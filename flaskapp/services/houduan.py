import pandas as pd
from sklearn import tree

data = pd.read_csv('verify.csv')
x = data.iloc[:, data.columns != "flag"]
y = data.iloc[:, data.columns == "flag"]

test = pd.read_csv('t.csv')

fenleiqi = tree.DecisionTreeClassifier(criterion="entropy", random_state=20, splitter="random")
fenleiqi = fenleiqi.fit(x, y.astype('int'))

flag = fenleiqi.predict(test)
print(flag)
