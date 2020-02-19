#!/usr/bin/env python

PATH = '/Users/scott/gitRepos/Sandbox/credit-risk-workshop-cpd/data/'
COPYFROM = PATH + 'german_credit_data.csv'
TOCOPY = PATH + 'personal_data.csv'
NEWFILE = PATH + 'personal_data_id.csv'

print('Writing existing data first column to ' + NEWFILE + '...')

try:
    f = open(TOCOPY, 'r+')
    y = open(COPYFROM, 'r')
    z = open(NEWFILE, 'w')

    for old, new in zip(y,f):

        uuid = old.split(',')[0]
        add_line = (uuid + ',' + new)
        z.write(add_line)
finally:
    f.close()
    y.close()
    z.close()
