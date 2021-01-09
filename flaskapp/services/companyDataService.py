# coding:utf-8
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier


def fenxi():
    ID = 29

    mapstrategy1 = {1: '零售业', 2: '服务业', 3: '工业',  4: '商业服务业',  5: '社区服务',  6: '交通运输业'}
    mapstrategy2 = {10: '有限责任公司', 20: '合伙企业',  30: '股份有限公司', 40: '农民专业合作社',  50: '集体所有制企业'}
    mapstrategy3 = {10: '自然人', 20: '企业法人'}
    df = pd.read_csv("t.csv", index_col='ID')

    try:
        industry = mapstrategy1[np.array(df.loc[[ID], ['行业']])[0][0]]
    except KeyError:
        industry = "未知"
    try:
        comType = mapstrategy2[np.array(df.loc[[ID], ['企业类型']])[0][0]]
    except KeyError:
        comType = "未知"
    try:
        personType = mapstrategy3[np.array(df.loc[[ID], ['控制人类型']])[0][0]]
    except KeyError:
        personType = "未知"

    regTime = int(np.array(df.loc[[ID], ['注册时间']])[0][0])
    regMoney = np.array(df.loc[[ID], ['注册资本']])[0][0]
    rate = np.array(df.loc[[ID], ['控制人持股比例']])[0][0]

    fengxianAvg = (np.array(df.loc[[ID], ['净利润_2015']])[0][0]+np.array(df.loc[[ID], ['净利润_2016']])[0][0]+np.array(df.loc[[ID], ['净利润_2017']])[0][0])/3
    fengxianAvgDiv = (abs(np.array(df.loc[[ID], ['净利润_2015']])[0][0]-fengxianAvg)+abs(np.array(df.loc[[ID], ['净利润_2016']])[0][0]-fengxianAvg)+abs(np.array(df.loc[[ID], ['净利润_2017']])[0][0]-fengxianAvg))/3
    fengxian = fengxianAvgDiv/fengxianAvg


    rongziSum = np.array(df.loc[[ID], ['项目融资和政策融资额度_2015']])[0][0]+np.array(df.loc[[ID], ['项目融资和政策融资额度_2016']])[0][0]+np.array(df.loc[[ID], ['项目融资和政策融资额度_2017']])[0][0]
    yilai = rongziSum/(fengxianAvg + 1)

    yingyeSum = np.array(df.loc[[ID], ['营业总收入_2015']])[0][0]+np.array(df.loc[[ID], ['营业总收入_2016']])[0][0]+np.array(df.loc[[ID], ['营业总收入_2017']])[0][0]
    zhouzhuan = yingyeSum/(np.array(df.loc[[ID], ['资产总额_2016']])[0][0]+1)

    fuzhaiSum = np.array(df.loc[[ID], ['负债总额_2015']])[0][0]+np.array(df.loc[[ID], ['负债总额_2016']])[0][0]+np.array(df.loc[[ID], ['负债总额_2017']])[0][0]
    fuzhai = fuzhaiSum/(np.array(df.loc[[ID], ['资产总额_2016']])[0][0]+1)

    dict = {}
    di = []

    dictt = {}

    dictt['id'] = ID
    dictt['industry'] = industry
    dictt['comType'] = comType
    dictt['personType'] = personType

    dictt['regTime'] = regTime
    dictt['regMoney'] = regMoney
    dictt['rate'] = rate

    dictt['fengxian'] = fengxian
    dictt['yilai'] = yilai
    dictt['zhouzhuan'] = zhouzhuan
    dictt['fuzhai'] = fuzhai

    di.append(dictt)
    dict["data"] = di
    return dict


def multiple():
    data = pd.read_csv("uploadfile/train.csv")
    x = data.iloc[:, data.columns != "flag"]
    y = data.iloc[:, data.columns == "flag"]

    test = pd.read_csv('uploadfile/verify.csv')
    Xtest = test.iloc[:, test.columns != "flag"]
    Ytest = test.iloc[:, test.columns == "flag"]

    fenleiqi = RandomForestClassifier(n_estimators=47, random_state=20)
    fenleiqi = fenleiqi.fit(x, y.astype('int').values.ravel())
    flag = fenleiqi.predict(Xtest)

    dict = {}
    di = []
    for i in range(0, len(Xtest)):
        dictt = {}

        id = Xtest.iloc[i]['ID']


        dictt['id'] = id
        if flag[i] == 1:
            dictt['flag'] = True
        else:
            dictt['flag'] = False
        di.append(dictt)

    dict["data"] = di

    return dict


# 在生产环境中弃用
def single():
    data = pd.read_csv("uploadfile/train.csv")
    x = data.iloc[:, data.columns != "flag"]
    y = data.iloc[:, data.columns == "flag"]

    test = pd.read_csv("uploadfile/uploadfile.t.csv")
    Xtest = test.iloc[:, test.columns != "flag"]

    fenleiqi = tree.DecisionTreeClassifier(criterion="entropy", random_state=20, splitter="random")
    fenleiqi = fenleiqi.fit(x, y.astype('int'))

    flag = fenleiqi.predict(Xtest)

    dict = {}
    di = {}
    tuple = []

    if flag == 1:
        di['flag'] = True
    else:
        di['flag'] = False

    tuple.append(di)

    dict['data'] = tuple

    return dict
