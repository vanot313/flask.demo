import torch
from algorithm.market.load_data import load_data
from algorithm.market.model import model
import time
import pandas as pd
import numpy as np



class MarketValuation:

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
        x = self.name_map('to_dimension.txt')

        df = pd.read_csv(address, index_col=0)
        df.fillna(0, inplace=True)

        # df.to_csv('predict/test.csv')
        # df.drop(['Unnamed: 0'], axis=1, inplace=True)

        # 清洗csv文件中数据。使用 x=x-min/max-min对每一列的值进行数据归一化，去掉前两行无用数据
        df1 = pd.read_csv('predict/fundamentals.csv', index_col=0)
        np.random.seed(1)
        df1 = df1.iloc[:, 2:78]
        df2 = (df - df1.min()) / (df1.max() - df1.min())

        # for i in range(5):
        #     for j in range(len(x[str(i+1)])):
        # print(j)
        # print(df.loc[0][x[str(i+1)][j]])

        # 创建5*25矩阵
        matrixA = np.zeros((5, 25))
        for j in range(5):
            for k in range(len(x[str(j + 1)])):
                if x[str(j + 1)][k] == 'Ticker Symbol' or x[str(j + 1)][k] == 'Period Ending':
                    continue
                temp = df2.loc[:, [x[str(j + 1)][k]]]
                # yy = float(df2.loc[i][x[str(j + 1)][k]])
                # print('i=',i,'j=',j,'k=',k,'\t',yy)
                matrixA[j][k] = float(temp.values)
            np.save('predict/test.npy', matrixA)
        matrixA2 = np.zeros((5,))
        for i in range(len(df2)):
            for j in range(5):
                matrixA2[j] = 10
            np.save('predict/save.npy', matrixA2)

        '''
        test = np.load('predict/test.npy')  # 加载文件
        save = np.load('predict/save.npy')  # 加载文件
        print("test", test)  # 将打印内容写入文件中
        print("save", save)  # 将打印内容写入文件中
        '''

        x = np.load('predict/test.npy')
        y = np.load('predict/save.npy')
        y = np.expand_dims(y, 1)
        save = np.concatenate((x, y), 1)
        np.save('predict/save/final.npy', save)

    def predict(self):
        device = torch.device("cpu")
        batch_size = 1

        base_path = 'predict/save'

        net = model().to(device)
        net = torch.load('save_model/440.pkl')
        train_loader = load_data(base_path, batch_size)

        correct = 0
        loss_mean = 0
        net.train()
        start = time.time()

        for i, data in enumerate(train_loader):
            inputs, labels = data

            p = net(inputs)

            predict = p.detach().numpy()
            predict_assets = ((predict[0] + 0) * (predict[1] + 0) * (predict[2] + 0) * (predict[3] + 0) * (
                    predict[4] + 0) - 1) * 16000000

            error = abs(516000000000 - predict_assets) / 516000000000

            print('维度预测结果：', predict)
            print('预测结果：', predict_assets)
            print("误差：", error)
            print('耗时：', time.time() - start)



mv = MarketValuation()
mv.load('../../uploadfile/market/d2yqM6MnjUP6zlbEOd4h.csv')
mv.predict()
