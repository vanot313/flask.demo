import pandas as pd

# 读取数据
data = pd.read_csv('data_JDWX.csv')
all = data.shape[0]

# 完整性
full = data.isnull().sum(axis=1).value_counts().iloc[0]/all
# percent = (data.isnull().sum() / data.shape[0]).sort_values(ascending=False).map(lambda x: "{:.2%}".format(x))
print('完整性: {:.2%}'.format(full))

# 正确性
right = data.loc[(data['browse'] <= 30000) & (data['evaluation'] == 5)].shape[0]  # 在代码中定义正确的数据定义（与$ 或|）
correct = right/all
print('正确性: {:.2%}'.format(correct))

# 一致性
uniformity = 0
print('一致性: {:.2%}'.format(uniformity))

# 重复性
repeat = data.duplicated().sum()/all
print('重复性: {:.2%}'.format(repeat))
