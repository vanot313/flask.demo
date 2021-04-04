import sys

import torch
from algorithm.market.load_data import load_data
from algorithm.market.model import model
import time
import pandas as pd
import numpy as np
import sys


class MarketValuationA:
    amount = 0
    size = 0
    growth = 0
    coverage = 0
    attribute = 0
    source = 0
    maintenance = 0
    incoming = 0
    outgoing = 0

    graininess = 0
    dimension = 0
    activity = 0
    scale = 0
    correlation = 0
    suggestion = 0

    # 读取txt文件内容，并按照序号分组
    def name_map(self, path):
        label_dict = {'1': [], '2': [], '3': [], '4': [], '5': []}
        fs = open(path, 'r')
        for f in fs:
            data = f.split("%")
            num = data[1].split('\n')
            label_dict[str(data[0])].append(num[0])

        return label_dict

    def load(self, address):
        # x = self.name_map('to_dimension.txt')
        x = self.name_map('algorithm/market/to_dimension.txt')

        df = pd.read_csv(address, index_col=0)
        df.fillna(0, inplace=True)

        # df.to_csv('predict/test.csv')
        # df.drop(['Unnamed: 0'], axis=1, inplace=True)

        # 清洗csv文件中数据。使用 x=x-min/max-min对每一列的值进行数据归一化，去掉前两行无用数据

        # df1 = pd.read_csv('predict/fundamentals.csv', index_col=0)
        df1 = pd.read_csv('algorithm/market/predict/fundamentals.csv', index_col=0)

        np.random.seed(1)
        df1 = df1.iloc[:, 2:78]
        df2 = (df - df1.min()) / (df1.max() - df1.min())

        # for i in range(5):
        #     for j in range(len(x[str(i+1)])):
        #         print(j)
        #         print(df.loc[0][x[str(i+1)][j]])

        # 创建5*25矩阵
        matrixA = np.zeros((5, 25))
        matrixA2 = np.zeros((5,))
        for i in range(5):
            matrixA2[i] = 10
        n = matrixA2
        n = np.expand_dims(n, 1)

        for i in range(len(df)):
            number = df.index[i]
            self.amount = (df.loc[number]['Total Revenue'] / 486000000000) * 10  # 数据量
            self.size = (df.loc[number]['Total Liabilities & Equity'] / 2570000000000) * 10  # 数据大小
            self.growth = (df.loc[number]['Total Liabilities'] / 2340000000000) * 10  # 数据增长速度
            self.coverage = (df.loc[number]['Total Equity'] / 256000000000) * 10  # 数据覆盖范围
            self.attribute = (df.loc[number]['Cash and Cash Equivalents'] / 728000000000) * 10  # 数据属性数量
            self.source = (df.loc[number]['Common Stocks'] / 158000000000) * 10  # 数据来源种类
            self.maintenance = (df.loc[number]['Depreciation'] / 29517000000) * 10  # 数据维护频率
            self.incoming = (df.loc[number]['Earnings Before Interest and Tax'] / 79053000000) * 10  # 流入数据频率
            self.outgoing = (df.loc[number]['Earnings Before Tax'] / 78726000000) * 10  # 流出数据频率

        for i in range(len(df2)):
            number = df.index[i]
            matrixA = np.zeros((5, 25))
            for j in range(5):
                for k in range(len(x[str(j + 1)])):
                    if x[str(j + 1)][k] == 'Ticker Symbol' or x[str(j + 1)][k] == 'Period Ending':
                        continue
                    temp = float(df2.loc[number][x[str(j + 1)][k]])
                    # print('i=', i, 'j=', j, 'k=', k, '\t', temp)
                    matrixA[j][k] = temp
            m = matrixA
            save = np.concatenate((m, n), 1)

            # np.save('predict/save/' + str(number) + '.npy', save)
            np.save('algorithm/market/predict/save/' + str(number) + '.npy', save)

    def predict(self):
        device = torch.device("cpu")
        batch_size = 1

        # base_path = 'predict/save'
        base_path = 'algorithm/market/predict/save'

        net = model().to(device)

        # net = torch.load('save_model/440.pkl')
        net = torch.load('algorithm/market/save_model/440.pkl')


        train_loader = load_data(base_path, batch_size)

        net.train()
        start = time.time()

        for i, data in enumerate(train_loader):
            inputs, labels = data

            p = net(inputs)

            predict = p.detach().numpy()
            predict_assets = ((predict[0] + 0) * (predict[1] + 0) * (predict[2] + 0) * (predict[3] + 0) * (
                    predict[4] + 0) - 1) * 16000000

            self.graininess = predict[0]  # 颗粒度
            self.dimension = predict[1]  # 多维度
            self.activity = predict[2]  # 活性度
            self.scale = predict[3]  # 规模度
            self.correlation = predict[4]  # 关联度
            self.suggestion = int(predict_assets/1000000)  # 资产评估建议

            # print('维度预测结果：', predict)
            # print('预测结果：', predict_assets)
            # print('耗时：', time.time() - start)


sys.path.append('algorithm/market')
#
# mv = MarketValuationA()
#
# # mv.load('../../uploadfile/market/d2yqM6MnjUP6zlbEOd4h.csv')
# mv.load('uploadfile/market/d2yqM6MnjUP6zlbEOd4h.csv')
#
# mv.predict()
#
#
# print("# 数据量", mv.amount)
# print("# 数据大小", mv.size)
# print("# 数据增长速度", mv.growth)
# print("# 数据覆盖范围", mv.coverage)
# print("# 数据属性数量", mv.attribute)
# print("# 数据来源种类", mv.source)
# print("# 数据维护频率", mv.maintenance)
# print("# 流入数据频率", mv.incoming)
# print("# 流出数据频率", mv.outgoing)
#
# print("# 颗粒度", mv.graininess)
# print("# 多维度", mv.dimension)
# print("# 活性度", mv.activity)
# print("# 规模度", mv.scale)
# print("# 关联度", mv.correlation)
# print("# 资产评估建议", int(mv.suggestion))

