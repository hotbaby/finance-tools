# encoding: utf8

import numpy as np


def finance_eaoi_irr(loan, repayment, total_index):
    """
    等额本息IRR
    :param loan: 借款金额
    :param repayment: 月还款额
    :param total_index: 总期次
    :return 月化利率
    """
    array = [repayment for _ in range(total_index)]
    array += [-loan]
    return -np.irr(array)


def finance_eaoi_annual_rate(loan, repayment, total_index):
    """
    等额本息年化利率
    :param loan: 借款金额
    :param repayment: 月还款额
    :param total_index: 总期次
    :return 年化利率
    """
    return finance_eaoi_irr(loan, repayment, total_index) * 12
