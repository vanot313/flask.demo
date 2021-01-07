import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('verify.csv')
x = data.iloc[:, data.columns != "flag"]
y = data.iloc[:, data.columns == "flag"]

test = pd.read_csv('train.csv')
Xtest = test.iloc[:, data.columns != "flag"]
Ytest = test.iloc[:, data.columns == "flag"]

fenleiqi = RandomForestClassifier(n_estimators=47, random_state=20)
fenleiqi = fenleiqi.fit(x, y.astype('int').values.ravel())
# score = fenleiqi.score(x, y.astype('int').values.ravel())
flag = fenleiqi.predict(Xtest)

dict = {}
di = []
for i in range(0, len(test)):
    dictt = []
    dictt.append(test.iloc[i]['ID'].astype('int'))
    if flag[i] == 1:
        dictt.append(True)
    else:
        dictt.append(False)
    di.append(dictt)

dict["data"] = di
print(dict)
