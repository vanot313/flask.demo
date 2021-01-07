import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('verify.csv')
x = data.iloc[:, data.columns != "flag"]
y = data.iloc[:, data.columns == "flag"]

test = pd.read_csv('t.csv')

fenleiqi = RandomForestClassifier(n_estimators=47, random_state=20)
fenleiqi = fenleiqi.fit(x, y.astype('int').values.ravel())

flag = fenleiqi.predict(test)
print(flag)
flag = pd.Series(flag)
print(flag.value_counts())
