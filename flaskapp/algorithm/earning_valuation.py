class EarningValuation:
    # 待评估数据资产的价值，最终结果
    P = 0

    ## 用户输入企业名
    name = ""
    ## ..........

    ## 专家输入数据
    # 待评估数据资产的预期获利持续年限
    n = 5
    # 待评估数据资产的折现率,需要依据实际情况变化
    r = 0.1
    # 第i年的预期收益
    R = []
    ## ..........

    def __init__(self):
        pass

    def getpar(self, n, r, R):
        self.n = n
        self.r = r
        self.R = R

    def calculate(self):
        # 计算收益法下的数据资产评估价值
        for i in range(1, self.n + 1):
            self.P = self.P + self.R[i - 1] / (1 + self.r) ** i


# c = earning_valuation()
# c.getpar(5, 0.1, [5000, 1000, 2000, 500, 200])
# print('数据资产的预期获利持续年限: {}'.format(c.n))
# print('数据资产的折现率: {}'.format(c.r))
# for i in range(0, c.n):
#     print('第 {} 年的预期收益: {}'.format(i, c.R[i]))
#
# c.calculate()
# print("用收益法计算获得的数据资产评估价值为", c.P)
