# coding:utf-8
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier


def multiple():
    data = pd.read_csv("services/verify.csv")
    x = data.iloc[:, data.columns != "flag"]
    y = data.iloc[:, data.columns == "flag"]

    test = pd.read_csv('services/train.csv')
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


def single():
    data = pd.read_csv("services/verify.csv")
    x = data.iloc[:, data.columns != "flag"]
    y = data.iloc[:, data.columns == "flag"]

    test = pd.read_csv("static/uploadfile.t.csv")
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
