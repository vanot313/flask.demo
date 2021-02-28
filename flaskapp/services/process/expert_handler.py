from services.algorithm.comprehensive_valuation import *
from services.algorithm.cost_valuation import *
from services.algorithm.earning_valuation import *
from common.models.work_order import WorkOrder
from common.models.comprehensive_valuation import ComprehensiveValuation
from common.models.cost_valuation import CostValuation
from common.models.earning_valuation import EarningValuation


def ExpertComprehensiveHandler(work_order_id, rareness, timeness, dimensional, economy, quality_weight, applied_weight):
    handler = comprehensive_valuation()

    # TODO 得到数据集文件安置的解决方案
    address = ""

    handler.quality_value(address)

    handler.applied_value(rareness, timeness, dimensional, economy)

    handler.matrix_value(quality_weight[0], quality_weight[1],
                         quality_weight[2], quality_weight[3],
                         quality_weight[4], quality_weight[5],
                         applied_weight[0], applied_weight[1],
                         applied_weight[2], applied_weight[3],
                         applied_weight[4], applied_weight[5])

    handler.calculate()

    # TODO 将估值数据存入数据库



    # TODO 并返回结果


    return 1


def ExpertCostHandler(work_order_id, R, C, II, M, E):
    handler = cost_valuation()
    handler.getpar(R, C, II, M, E)
    handler.calculate()

    # TODO 将估值数据存入数据库
    # TODO 并返回结果
    return 1


def ExpertEarningHandler(work_order_id, n, r, R):
    handler = earning_valuation()
    handler.getpar(n, r, R)
    handler.calculate()


    # TODO 将估值数据存入数据库
    # TODO 并返回结果
    return 1