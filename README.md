# 数据预处理

## 对数据的理解

一般来说，直接获取的数据往往是不完美的。由于各种因素，数据往往存在空缺、错误以及无效字段。直接处理这样的数据是不现实的，大大影响处理效率、正确率，所以需要对其进行预处理。

## 对数据的处理

根据获得数据的具体需求进行处理。一般需要如下处理：

### 将数据读取到内存中

```python
data = pd.read_csv('xxx.csv', engine='python', encoding="gbk")
```

### 合并数据

所获得的数据可能不止存在于一张表中，这时候就需要依据某些数据（主键）合并表，将信息富集到一张表中

```python
# 合并base_train和knowledge_train,依据ID字段
base_knowledge_train = pd.merge(base_train_data, knowledge_train, on='ID', how='inner')

# 处理money_train和year_train,依据ID和year字段
money_year_train = pd.merge(money_train, year_train, on=['ID', 'year'])

# 还有rename、add_suffix等操作，辅助合并数据，查文档可以看
```

### 数据清洗

1. 对重复值进行处理

   ```python
   # 查看是否有重复值
   data.duplicated().value_counts()
   
   # 删除重复行
   '''
   duplicates(subset,keep,inplace)
   subset:以哪几列作为基准列，判断是否重复，如果不写则默认所有列都要重复才算
   keep: 保留哪一个，fist-保留首次出现的，last-保留最后出现的，False-重复的一个都不保留，默认为first
   inplace: 是否进行替换，最好选择False，保留原始数据，默认也是False
   '''
   data.drop_duplicates(subset=["ID1","ID2"],keep='first',inplace=True)
   ```

   

2. 对缺失值进行处理

```python
# 查看是否有空值（输出整个表的情况，有空值显示True，没空值显示False）
data.isnull()

# 查看是哪一列有空值
data.isnull().any()

# 删除所有含缺失值的行
'''
dropna(axis,subset,how,thresh,inplace)
axis: 删除行还是列，行是0或index,列是1或column，默认是行
subst: 删除某几列的缺失值，可选，默认为所有列
how: any or all，any表明只要出现1个就删除，all表示所有列均为NaN才删
thresh: 缺失值的数量标准，达到这个阈值才会删除
inplace: 是否替换
'''
df1.dropna(how='any')

# 填充缺失值
'''
fillna(value,method,{},limit,inplace,axis)
value: 可以传入一个字符串或数字替代NaN，值可以是指定的或者平均值，众数或中位数等
method: 有ffill（用前一个填充）和bfill（用后一个填充）两种
{}： 可以根据不同的列填充不同的值，列为键，填充值为值
limit: 限定填充的数量
inplace: 是否直接在原文件修改
axis: 填充的方向，默认是0，按行填充
'''
df1.fillna(value=5)

# 缺失值插值
拉格朗日插值缺失值，如果用到再说

# 提取 nan 值的布尔掩码（NaN的输出True，其他输出False）
pd.isna(df1)
```
3. 对异常值进行处理

```python
# 描述性分析
data.describe()

# 画散点图观察
from matplotlib import pyplot as plt
plt.scatter(data["数量"], data[" 销售金额 "])
plt.show()

# 画箱型图观察
from matplotlib import pyplot as plt
plt.scatter(data["数量"], data[" 销售金额 "])
plt.show()

# 人工观察
使用其他方法观察

# 删除异常值
将异常值替换为NaN，然后当作缺失值删除

# 替换异常值
将异常值替换为NaN，然后当作缺失值替换，替换成什么得看具体情况

```

### 特征工程

经过上述处理后的数据还算不错，可以直接进行模型训练了，但是还可以处理得更好。不同字段的重要性不同，可以在开始模型训练之前对一些字符（特征）进行初步筛选

特征工程就是将原始数据转换为更能代表预测模型的潜在问题的特征的过程，可以通过挑选最相关的特征，提取特征以及创造特征来实现。其中创造特征又经常以降维算法的方式实现

可能面对的问题有：①特征之间有相关性 ②特征和标签无关 ③特征太多或太小，或者干脆就无法表现出应有的数据现象或无法展示数据的真实面貌
特征工程的目的：① 降低计算成本 ②提升模型上限

*可以较为简单，也可以非常复杂，也是提升算法的一部分*