import pandas as pd
import numpy as np


class comprehensive_valuation:
    # 判断的文件路径
    address = ""
    # 完整性
    __full = 0.0
    # 正确性
    __correct = 0.0
    # 一致性
    __uniformity = 0.0
    # 重复性
    __repeat = 0.0

    # 稀缺性
    __rareness = 0.0
    # 时效性
    __timeliness = 0.0
    # 多维性
    __dimensional = 0.0
    # 场景经济性
    __economy = 0.0

    # 质量矩阵权重
    __quality_weight = []

    # 应用矩阵权重
    __applied_weight = []

    def __init__(self):
        pass

    # 质量价值评估 分析数据表
    def quality_value(self, address):
        self.address = address

        # 读取数据
        data = pd.read_csv(self.address)
        # data = pd.read_csv('../uploadfile/uploadfile.data_JDWX.csv')
        all = data.shape[0]

        # 完整性
        full = data.isnull().sum(axis=1).value_counts().iloc[0] / all
        # percent = (data.isnull().sum() / data.shape[0]).sort_values(ascending=False).map(lambda x: "{:.2%}".format(x))
        print('完整性: {:.2%}'.format(full))
        self.__full = full

        # 正确性
        right = data.loc[(data['browse'] <= 30000) & (data['evaluation'] == 5)].shape[0]  # 在代码中定义正确的数据定义（与$ 或|）
        correct = right / all
        print('正确性: {:.2%}'.format(correct))
        self.__correct = correct

        # 一致性
        uniformity = 0
        print('一致性: {:.2%}'.format(uniformity))
        self.__uniformity = uniformity

        # 重复性
        repeat = data.duplicated().sum() / all
        print('重复性: {:.2%}'.format(repeat))
        self.__repeat = repeat

    # 应用价值评估 专家打分法
    def applied_value(self, r, t, d, e):
        self.__rareness = r
        print('稀缺性: {:.2%}'.format(self.__rareness))

        self.__timeliness = t
        print('时效性: {:.2%}'.format(self.__timeliness))

        self.__dimensional = d
        print('多维性: {:.2%}'.format(self.__dimensional))

        self.__economy = e
        print('场景经济性: {:.2%}'.format(self.__economy))

    # 输入矩阵参数 构造权重向量 专家打分法
    def matrix_value(self, fc, fu, fr, cu, cr, ur,
                     rt, rd, re, td, te, de):
        mat_quality = np.array([[1, fc, fu, fr],
                                [1 / fc, 1, cu, cr],
                                [1 / fu, 1 / cu, 1, ur],
                                [1 / fr, 1 / cr, 1 / ur, 1]
                                ])

        mat_applied = np.array([[1, rt, rd, re],
                                [1 / rt, 1, td, te],
                                [1 / rd, 1 / td, 1, de],
                                [1 / re, 1 / te, 1 / de, 1]
                                ])

        weight_quality = self.get_weight(mat_quality)
        if len(weight_quality) == 0:
            print("质量对比矩阵未通过一致性检验，需对对比矩阵重新构造")
            return False

        weight_applied = self.get_weight(mat_applied)
        if len(weight_applied) == 0:
            print("应用对比矩阵未通过一致性检验，需对对比矩阵重新构造")
            return False

        self.__quality_weight = weight_quality
        self.__applied_weight = weight_applied

    # 计算最终价值
    def calculate(self):
        Sq = self.__quality_weight[0] * self.__full + \
             self.__quality_weight[1] * self.__correct + \
             self.__quality_weight[2] * (1 - self.__uniformity) + \
             self.__quality_weight[3] * (1 - self.__repeat)
        Sa = self.__applied_weight[0] * self.__rareness + \
             self.__applied_weight[1] * self.__timeliness + \
             self.__applied_weight[2] * self.__dimensional + \
             self.__applied_weight[3] * self.__economy

        Sq = Sq*100
        Sa = Sa*100

        print("质量价值估分 {:.3f}".format(Sq))
        print("应用价值估分 {:.3f}".format(Sa))

        S = (Sa * Sq) / 100

        print("资产价值估分 {:.3f}".format(S))

    # 根据特征法计算矩阵权重
    def get_weight(self, mat):
        m = len(mat)  # 获取指标个数
        n = len(mat[0])
        RI = [0, 0, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51]
        R = np.linalg.matrix_rank(mat)  # 求判断矩阵的秩
        V, D = np.linalg.eig(mat)  # 求判断矩阵的特征值和特征向量，V特征值，D特征向量；
        list1 = list(V)
        B = np.max(list1)  # 最大特征值
        index = list1.index(B)
        C = D[:, index]  # 对应特征向量
        CI = (B - n) / (n - 1)  # 计算一致性检验指标CI
        CR = CI / RI[n]
        if CR < 0.10:
            print("CI=", CI)
            print("CR=", CR)
            print('对比矩阵通过一致性检验，各向量权重向量Q为：')
            sum = np.sum(C)

            Q = C / sum  # 特征向量标准化
            print(Q)
            return Q  # 输出权重向量
        else:
            return []


c = comprehensive_valuation()
c.quality_value('../uploadfile/uploadfile.data_JDWX.csv')
c.applied_value(0.8, 0.2, 0.5, 0.5)
c.matrix_value(1, 3, 5, 3, 5, 3, 1/3, 1/5, 1/9, 1/3, 1/3, 1/3)
c.calculate()
