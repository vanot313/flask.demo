import matplotlib.pyplot as plt
import tensorflow_datasets as tfds
import tensorflow as tf
from tensorflow.keras import Sequential, layers



# 利用 matplotlib 可视化训练过程
# 解决中文乱码问题
# 字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 字体大小
plt.rcParams['font.size'] = 20

def plot_graphs(history, name):
    # 描点
    plt.plot(history.history[name])
    plt.plot(history.history['val_' + name])
    # 横坐标为迭代次数
    plt.xlabel("Epochs")
    # 纵坐标为设置的参数（如准确率 accuracy）
    plt.ylabel(name)
    # 备注版
    plt.legend([name, 'val_' + name])
    # 呈现
    plt.show()

# 获取数据集。默认返回形式为字典，可以设置为以元组返回（ as_supervised ）
ds, info = tfds.load('imdb_reviews/subwords8k', with_info=True,
                          as_supervised=True)

# 获取训练集，测试集
train_ds, test_ds = ds['train'], ds['test']

# 设置缓冲区大小，批大小
BUFFER_SIZE, BATCH_SIZE = 10000, 64

# 打乱 BUFFER_SIZE 缓冲区大小内的数据，并始终保持缓冲区大小的乱序数据（不精确的理解）
train_ds = train_ds.shuffle(BUFFER_SIZE)

# 用于处理变长序列，将其补长至一样的长度
# BATCH_SIZE 为 每一批处理的样本数量
# BATCH_SHAPES 为 每一批数据的样本的大小，默认为 -1 即补齐至最长的样本长度
train_ds = train_ds.padded_batch(BATCH_SIZE, tf.compat.v1.data.get_output_shapes(train_ds))
test_ds = test_ds.padded_batch(BATCH_SIZE, tf.compat.v1.data.get_output_shapes(test_ds))

# 批次数
count = 0
# 示例：打印经过 padded_batch 处理完成后的元组
for item in train_ds.as_numpy_iterator():
   count += 1
   print("*" * 20)
   print(item)
print(count)


# 获取 tokenizer。用进行字符处理级id转换（这里先转换成 subword，再转换为 id）等操作（即先转换为单词再给单词打上编号）
# 总之从结果上来看的话，这里完成对字符文本串的序列化，因为 RNN 或者说所有的 NN 是处理数字的神经网络，需要将文本变成数字编号才能进行训练
tokenizer = info.features['text'].encoder
print ('词汇个数:', tokenizer.vocab_size)

# 示例：试着将这句话中的单词进行分解编码
# sample_str = 'it is write by vanot313.'
# tokenized_str = tokenizer.encode(sample_str)
# print ('向量化文本:', tokenized_str)
# 打印结果
# for ts in tokenized_str:
#     print (ts, '-->', tokenizer.decode([ts]))

# 借助 kera 来搭建 RNN 模型

model = Sequential([
    # 嵌入层。必须位于第一层，将正整数（下标）转换为具有固定大小的向量，如[[4],[20]]->[[0.25,0.1],[0.6,-0.2]]
    # 将纯粹的以数字表示的单词转换为固定维度的向量，词义相近的单词的向量也会相近，其本身也是参与训练的一层。
    # 需要区分 嵌入层 embedding 与 输入层 input 的区别
    layers.Embedding(tokenizer.vocab_size, 64),
    # 用双向 RNN 包装器包装 LSTM 层。
    # 这里还可以添加更多的 LSTM 层来增加性能。
    layers.Bidirectional(layers.LSTM(64)),
    # Dense：全连接层。
    # 采用 relu 函数来做激活函数。
    # 其他关键参数意义（在这里没有作为参数输入）：
    # kernel：权值矩阵
    # bias：偏置（偏差）向量
    layers.Dense(64, activation='relu'),
    # 全连接层（输出），采用 sigmoid 函数来做输出激活函数
    layers.Dense(1, activation='sigmoid')
])

# model.compile 编译创建好的模型，网络模型搭建完后，需要对网络的学习过程进行配置，否则在调用 fit 或 evaluate 时会抛出异常。
model.compile(loss='binary_crossentropy', optimizer='adam',
              metrics=['accuracy'])

# 使用现有模型
USE_WEIGHT = True
# 做测试集测试
DO_TEST = False

if not USE_WEIGHT:
    # 训练，迭代三次。不过这里相较于之前自己写的 demo 训练的参数只设置了迭代次数。
    history1 = model.fit(train_ds, epochs=10, validation_data=test_ds)
    # 保存模型
    model.save("testmodle")
    model.save_weights("testmodle_weight")
    # 绘制迭代图像
    plot_graphs(history1, 'accuracy')
    plot_graphs(history1, 'loss')
else:
    # 加载已有模型
    model.load_weights("testmodle_weight")

if DO_TEST:
    # 和之前自己写的简单 demo 一样。evaluate 函数代表估值函数，即输入测试集，进行完整的测试。
    loss, acc = model.evaluate(test_ds)

    print('准确率:', acc)
    print('损失函数值：', loss)






