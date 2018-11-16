#!/usr/bin/env python

import click

from finance_tools import finance_eaoi_annual_rate


@click.command('eaoi')
@click.argument('loan')
@click.argument('repayment')
@click.argument('index')
def cli(loan, repayment, index):
    loan = float(loan)
    repayment = float(repayment)
    index = int(index)
    annual_rate = finance_eaoi_annual_rate(loan, repayment, index)
    print 'loan: %s repayment: %s index: %s' % (loan, repayment, index)
    print 'annual rate: %s' % round(annual_rate * 100, 4) + '%'
