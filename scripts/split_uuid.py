#!/usr/bin/env python

PATH = '/Users/scott/gitRepos/Sandbox/credit-risk-workshop-cpd/data/'
COPYFROM = PATH + 'german_credit_data.csv'
FINANCIAL = PATH + 'financial_data.csv'
NONFINANCIAL = PATH + 'non_financial_data.csv'

print('Spliting file into 2 ...')

with open(COPYFROM, 'r') as original:
    with open(FINANCIAL, 'w') as financial:
        with open(NONFINANCIAL, 'w') as nonfinancial:
            for line in original:
                first = line.split(',')[:6]
                first = ",".join(str(x) for x in first)
                last = line.split(',')[6:]
                uuid = line.split(',')[0]
                last = ",".join(str(x) for x in last)
                last = uuid + ',' + last

                financial.write(first + '\n')
                nonfinancial.write(last + '\n')

