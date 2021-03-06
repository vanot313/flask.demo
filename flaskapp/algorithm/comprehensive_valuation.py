import pandas as pd
import numpy as np

FILE_ERROR = 1
Q_ERROR = 2
A_ERROR = 3

SUCCESS = 0


class ComprehensiveValuationA:
    ## 用户输入参数（在这里指文件本身）
    # 判断的文件路径
    address = ""
    ## ----------

    # 完整性
    full = 0.0
    # 正确性
    correct = 0.0
    # 一致性
    uniformity = 0.0
    # 重复性
    repeat = 0.0

    ## 专家输入参数
    # 稀缺性
    rareness = 0.0
    # 时效性
    timeliness = 0.0
    # 多维性
    dimensional = 0.0
    # 场景经济性
    economy = 0.0

    # 质量矩阵权重
    quality_weight = []
    # 应用矩阵权重
    applied_weight = []
    ## ----------

    # RI 参数
    RI = [0, 0, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51]

    # 质量价值得分
    Sq = 0
    # 应用价值得分
    Sa = 0

    # 总价值得分
    S = 0

    def __init__(self):
        pass

    # 质量价值评估 分析数据表
    def quality_value(self, address):

        self.address = address

        try:
            # 读取数据
            data = pd.read_csv(self.address)
        except:
            return FILE_ERROR

        # data = pd.read_csv('../uploadfile/uploadfile.data_JDWX.csv')
        all = data.shape[0]

        # 完整性
        full = data.isnull().sum(axis=1).value_counts().iloc[0] / all
        # percent = (data.isnull().sum() / data.shape[0]).sort_values(ascending=False).map(lambda x: "{:.2%}".format(x))
        print('完整性: {:.2%}'.format(full))
        self.full = full

        # 正确性
        right = data.loc[(data['browse'] <= 30000) & (data['evaluation'] == 5)].shape[0]  # 在代码中定义正确的数据定义（与$ 或|）
        correct = right / all
        print('正确性: {:.2%}'.format(correct))
        self.correct = correct

        # 一致性
        uniformity = 0
        print('一致性: {:.2%}'.format(uniformity))
        self.uniformity = uniformity

        # 重复性
        repeat = data.duplicated().sum() / all
        print('重复性: {:.2%}'.format(repeat))
        self.repeat = repeat

        return SUCCESS

    # 应用价值评估 专家打分法
    def applied_value(self, r, t, d, e):

        self.rareness = r
        print('稀缺性: {:.2%}'.format(self.rareness))

        self.timeliness = t
        print('时效性: {:.2%}'.format(self.timeliness))

        self.dimensional = d
        print('多维性: {:.2%}'.format(self.dimensional))

        self.economy = e
        print('场景经济性: {:.2%}'.format(self.economy))
        return SUCCESS

    # 输入矩阵参数 构造权重向量 专家打分法
    def matrix_value(self, weight, applied):
        weight_factor_0 = 1 / weight[0]
        weight_factor_1 = 1 / weight[1]
        weight_factor_2 = 1 / weight[2]
        weight_factor_3 = 1 / weight[3]
        weight_factor_4 = 1 / weight[4]
        weight_factor_5 = 1 / weight[5]

        mat_quality = np.array([[1, weight[0], weight[1], weight[2]],
                                [weight_factor_0, 1, weight[3], weight[4]],
                                [weight_factor_1, weight_factor_3, 1, weight[5]],
                                [weight_factor_2, weight_factor_4, weight_factor_5, 1]
                                ])

        mat_applied = np.array([[1, 1 / applied[0], 1 / applied[1], 1 / applied[2]],
                                [applied[0], 1, 1 / applied[3], 1 / applied[4]],
                                [applied[1], applied[3], 1, 1 / applied[5]],
                                [applied[2], applied[4], applied[5], 1]
                                ])

        weight_quality = self.get_weight(mat_quality)

        if len(weight_quality) == 0:
            print("质量对比矩阵未通过一致性检验，需对对比矩阵重新构造")
            return Q_ERROR

        weight_applied = self.get_weight(mat_applied)
        if len(weight_applied) == 0:
            print("应用对比矩阵未通过一致性检验，需对对比矩阵重新构造")
            return A_ERROR

        self.quality_weight = weight_quality
        self.applied_weight = weight_applied
        return SUCCESS

    # 计算最终价值
    def calculate(self):
        Sq = self.quality_weight[0] * self.full + \
             self.quality_weight[1] * self.correct + \
             self.quality_weight[2] * (1 - self.uniformity) + \
             self.quality_weight[3] * (1 - self.repeat)
        Sa = self.applied_weight[0] * self.rareness + \
             self.applied_weight[1] * self.timeliness + \
             self.applied_weight[2] * self.dimensional + \
             self.applied_weight[3] * self.economy

        Sq = Sq * 100
        Sa = Sa * 100

        print("质量价值估分 {:.3f}".format(Sq))
        print("应用价值估分 {:.3f}".format(Sa))
        S = (Sa * Sq) / 100

        print("资产价值估分 {:.3f}".format(S))
        self.Sq = Sq
        self.Sa = Sa
        self.S = S

        self.transfer_weight()
        return SUCCESS

    # 根据特征法计算矩阵权重
    def get_weight(self, mat):
        m = len(mat)  # 获取指标个数
        n = len(mat[0])
        R = np.linalg.matrix_rank(mat)  # 求判断矩阵的秩
        V, D = np.linalg.eig(mat)  # 求判断矩阵的特征值和特征向量，V特征值，D特征向量；
        list1 = list(V)
        B = np.max(list1)  # 最大特征值
        index = list1.index(B)
        C = D[:, index]  # 对应特征向量
        CI = (B - n) / (n - 1)  # 计算一致性检验指标CI
        CR = CI / self.RI[n]
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

    def transfer_weight(self):
        for i in range(0, 3):

            self.applied_weight[i] = str(self.applied_weight[i].real)
            print(self.applied_weight[i])
            self.quality_weight[i] = self.quality_weight[i].real
            print(self.quality_weight[i])

# c = ComprehensiveValuationA()
# c.quality_value('../uploadfile/6tSiFTUE2E8J7QRKl52D.csv')
# c.applied_value(0.8, 0.2, 0.5, 0.5)
# c.matrix_value([1, 3, 5, 3, 5, 3],[ 3, 5, 9, 3, 3, 3])
# c.calculate()
