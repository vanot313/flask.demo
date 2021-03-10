import pandas as pd
import csv
import numpy as np
import os

# 读取txt标定文件
path_txt = './data1.txt'


# 读取txt文件内容，并按照序号分组
def name_map(path):
    label_dict = {'1': [], '2': [], '3': [], '4': [], '5': []}
    fs = open(path, 'r')
    for f in fs:
        data = f.split("%")
        num = data[1].split('\n')
        label_dict[str(data[0])].append(num[0])

    return label_dict


x = name_map(path_txt)
# 输出已经分好组的列名
print(x)
# 将csv文件中null的地方补0，只需跑一次
# df = pd.read_csv('fundamentals.csv')
# df.fillna(0,inplace=True)
# df.to_csv('fundamentals.csv')
# df.drop(['Unnamed: 0'],axis=1,inplace=True)
#
# print(x)


# 清洗csv文件中数据。使用 x=x-min/max-min对每一列的值进行数据归一化，去掉前两行无用数据
df = pd.read_csv('fundamentals.csv')
np.random.seed(1)
df1 = df.iloc[:, 2:79]
df2 = (df1 - df1.min()) / (df1.max() - df1.min())
# print(df2)

# for i in range(5):
#     for j in range(len(x[str(i+1)])):
# print(j)
# print(df.loc[0][x[str(i+1)][j]])
# 创建5*25矩阵
matrixA = np.zeros((5, 25))
print(matrixA.shape)
# 将csv文件中的数据每一行列名对应的归一化数据写入创建的矩阵，保存为‘npy’。生成1780个npy数据，并生成与之对应的随机数组进行监督训练
for i in range(len(df2)):
    matrixA = np.zeros((5, 25))
    for j in range(5):
        for k in range(len(x[str(j + 1)])):
            # print(x[str(j+1)][k])
            if x[str(j + 1)][k] == 'Ticker Symbol' or x[str(j + 1)][k] == 'Period Ending':
                continue
            # print(float(df.loc[i][x[str(j+1)][k]]))
            yy = float(df2.loc[i][x[str(j + 1)][k]])
            # print('i=',i,'j=',j,'k=',k,'\t',yy)
            matrixA[j][k] = yy
    np.save('./save/' + str(i) + ".npy", matrixA)
    np.save('./save1/' + str(i) + ".npy", np.random.rand(5))
print(matrixA)
# np.save("filename.npy",a)
'''for i in range(5):
    matrixA[i]=[0]*m
print(matrixA)'''
test = np.load('./save1/0.npy')  # 加载文件
print(test)  # 将打印内容写入文件中
