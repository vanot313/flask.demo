# coding:utf-8

import pandas as pd


def buildTestFile():
    mapstrategy1 = {'零售业': 1, '服务业': 2, '工业': 3, '商业服务业': 4, '社区服务': 5, '交通运输业': 6}
    mapstrategy2 = {'有限责任公司': 10, '合伙企业': 20, '股份有限公司': 30, '农民专业合作社': 40, '集体所有制企业': 50}
    mapstrategy3 = {'自然人': 10, '企业法人': 20}

    base_test = pd.read_csv('uploadfile/uploadfile.base_test_sum.csv', engine='python', encoding="utf8")
    knowledge_test = pd.read_csv('uploadfile/uploadfile.knowledge_test_sum.csv', engine='python', encoding="utf8")
    money_test = pd.read_csv('uploadfile/uploadfile.money_report_test_sum.csv', engine='python', encoding="utf8")
    year_test = pd.read_csv('uploadfile/uploadfile.year_report_test_sum.csv', engine='python', encoding="utf8")

    base_test['行业'] = base_test['行业'].map(mapstrategy1)
    base_test['企业类型'] = base_test['企业类型'].map(mapstrategy2)
    base_test['控制人类型'] = base_test['控制人类型'].map(mapstrategy3)
    base_test_data = base_test.drop(columns=["区域"])
    # print(base_verify1)

    for column in list(base_test_data.columns[base_test_data.isnull().sum() > 0]):
        a = base_test_data[column].mean()
        base_test_data[column].fillna(a, inplace=True)

    for column in list(knowledge_test.columns[knowledge_test.isnull().sum() > 0]):
        a = round(knowledge_test[column].mean())
        knowledge_test[column].fillna(a, inplace=True)

    # 合并base_train和knowledge_train
    base_knowledge_test = pd.merge(base_test_data, knowledge_test, on='ID', how='inner')
    # print(base_knowledge_verify1)
    # 处理money_train和year_train,先根据ID和year合并两个数据
    money_year_test = pd.merge(money_test, year_test, on=['ID', 'year'])


    # 将2015，2016，2017年的数据分别提取出来

    money_year_test_2015 = money_year_test.loc[money_year_test['year'] == 2015].add_suffix('_2015')
    money_year_test_2015.rename(columns={'ID_2015': 'ID', 'year_2015': 'year'}, inplace=True)

    money_year_test_2016 = money_year_test.loc[money_year_test['year'] == 2016].add_suffix('_2016')
    money_year_test_2016.rename(columns={'ID_2016': 'ID', 'year_2016': 'year'}, inplace=True)

    money_year_test_2017 = money_year_test.loc[money_year_test['year'] == 2017].add_suffix('_2017')
    money_year_test_2017.rename(columns={'ID_2017': 'ID', 'year_2017': 'year'}, inplace=True)

    # 将151617合并成一张表

    money_year_test_20152016 = pd.merge(money_year_test_2015, money_year_test_2016, on='ID')
    # print(money_year_test_20152016)
    money_year_test_151617 = pd.merge(money_year_test_20152016, money_year_test_2017, on='ID')
    # print(money_year_test_2017)
    # 将money_year_test_151617和之前获得的base_knowledge_test表合在一起

    test_data = pd.merge(money_year_test_151617, base_knowledge_test, on='ID')
    print(money_year_test_151617)
    # 将"year_x","year_y","year"三列去除，因为这三列丝毫不影响该公司是否为僵尸企业，年度特征我们已经通过加后缀来区分（可以用PCA降维来说明）

    test_data = test_data.drop(columns=["year_x", "year_y", "year"])

    # 再一次对缺失值用均值填充：

    for column in list(test_data.columns[test_data.isnull().sum() > 0]):
        a = int(test_data[column].mean())
        test_data[column].fillna(a, inplace=True)
    # 最终的训练数据：
    test_data.to_csv("uploadfile/test.csv")


def buildVertifyFile():
    # 读取四份训练集csv文件

    mapstrategy1 = {'零售业': 1, '服务业': 2, '工业': 3, '商业服务业': 4, '社区服务': 5, '交通运输业': 6}
    mapstrategy2 = {'有限责任公司': 10, '合伙企业': 20, '股份有限公司': 30, '农民专业合作社': 40, '集体所有制企业': 50}
    mapstrategy3 = {'自然人': 10, '企业法人': 20}

    base_verify1 = pd.read_csv('datasets/base_verify1.csv', engine='python', encoding="utf-8-sig")
    knowledge_verify1 = pd.read_csv('datasets/paient_information_verify1.csv', engine='python', encoding="utf-8-sig")
    money_verify1 = pd.read_csv('datasets/money_information_verify1.csv', engine='python', encoding="utf-8-sig")
    year_verify1 = pd.read_csv('datasets/year_report_verify1.csv', engine='python', encoding="utf-8-sig")

    base_verify1['行业'] = base_verify1['行业'].map(mapstrategy1)
    base_verify1['企业类型'] = base_verify1['企业类型'].map(mapstrategy2)
    base_verify1['控制人类型'] = base_verify1['控制人类型'].map(mapstrategy3)
    base_verify1_data = base_verify1.drop(columns=["区域"])
    # print(base_verify1)

    for column in list(base_verify1_data.columns[base_verify1_data.isnull().sum() > 0]):
        a = base_verify1_data[column].mean()
        base_verify1_data[column].fillna(a, inplace=True)

    for column in list(knowledge_verify1.columns[knowledge_verify1.isnull().sum() > 0]):
        a = round(knowledge_verify1[column].mean())
        knowledge_verify1[column].fillna(a, inplace=True)

    # 合并base_train和knowledge_train
    base_knowledge_verify1 = pd.merge(base_verify1_data, knowledge_verify1, on='ID', how='inner')
    # print(base_knowledge_verify1)
    # 处理money_train和year_train,先根据ID和year合并两个数据
    money_year_verify1 = pd.merge(money_verify1, year_verify1, on=['ID', 'year'])


    # 将2015，2016，2017年的数据分别提取出来

    money_year_verify1_2015 = money_year_verify1.loc[money_year_verify1['year'] == 2015].add_suffix('_2015')
    money_year_verify1_2015.rename(columns={'ID_2015': 'ID', 'year_2015': 'year'}, inplace=True)

    money_year_verify1_2016 = money_year_verify1.loc[money_year_verify1['year'] == 2016].add_suffix('_2016')
    money_year_verify1_2016.rename(columns={'ID_2016': 'ID', 'year_2016': 'year'}, inplace=True)

    money_year_verify1_2017 = money_year_verify1.loc[money_year_verify1['year'] == 2017].add_suffix('_2017')
    money_year_verify1_2017.rename(columns={'ID_2017': 'ID', 'year_2017': 'year'}, inplace=True)

    # 将151617合并成一张表

    money_year_verify1_20152016 = pd.merge(money_year_verify1_2015, money_year_verify1_2016, on='ID')
    # print(money_year_verify1_20152016)
    money_year_verify1_151617 = pd.merge(money_year_verify1_20152016, money_year_verify1_2017, on='ID')
    # print(money_year_verify1_2017)
    # 将money_year_train_151617和之前获得的base_knowledge_train表合在一起

    verify1_data = pd.merge(money_year_verify1_151617, base_knowledge_verify1, on='ID')
    print(money_year_verify1_151617)
    # 将"year_x","year_y","year"三列去除，因为这三列丝毫不影响该公司是否为僵尸企业，年度特征我们已经通过加后缀来区分（可以用PCA降维来说明）

    verify1_data = verify1_data.drop(columns=["year_x", "year_y", "year"])

    # 再一次对缺失值用均值填充：

    for column in list(verify1_data.columns[verify1_data.isnull().sum() > 0]):
        a = int(verify1_data[column].mean())
        verify1_data[column].fillna(a, inplace=True)
    verify1_data = verify1_data.drop(columns=["控制人ID"])
    # 最终的训练数据：
    verify1_data.to_csv("uploadfile/verify.csv")
