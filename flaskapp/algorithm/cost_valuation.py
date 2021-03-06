class CostValuationA:
    # 待评估数据资产的价值，最终结果
    P = 0

    ## 用户输入企业名
    name = ""
    ## ..........

    ## 专家输入数据
    # 数据集成本投资收益率
    R = 0.1
    # 数据集重置成本
    C = 100000
    # 固有价值因素修正系数
    II = 1
    # 数据集的市场价值因素修正系数
    M = 1
    # 数据集的环境约束因素修正系数
    E = 1
    ## ..........

    def __init__(self):
        pass

    def getpar(self, r, c, ii, m, e):
        self.R = r
        self.C = c
        self.II = ii
        self.M = m
        self.E = e

    def calculate(self):
        p = self.C * (1 + self.R) * self.II * self.M * self.E
        self.P = p


# c = cost_valuation()
# c.getpar(0.1, 100000, 1, 1, 1)
# print('数据集成本投资收益率: {}'.format(c.R))
# print('数据集重置成本: {}'.format(c.C))
# print('故有价值因素修正系数: {}'.format(c.II))
# print('数据集市场价值因素修正系数: {}'.format(c.M))
# print('数据集环境约束因素修正系数: {}'.format(c.E))
#
# c.calculate()
# print('数据资产价值预估: {}'.format(c.P))
