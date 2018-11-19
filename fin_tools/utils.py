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


def finance_num2str(amount):
    """
    金额转换成字符串
    :param amount: 金额（元）
    :return amount_str
    """
    amount_integer, amount_decial = str(float(amount)).split('.')
    amount_integer = int(amount_integer)
    amount_decial = amount_decial
    amount_integer_split_list = []

    while amount_integer:
        s = str(amount_integer % 1000)
        amount_integer /= 1000
        s = s.zfill(3) if amount_integer else s
        amount_integer_split_list.append(s)

    return '%s.%s' % (','.join(amount_integer_split_list[::-1]), amount_decial)
