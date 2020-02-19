#!/usr/bin/env python

import uuid

PATH = '/Users/scott/gitRepos/Sandbox/credit-risk-workshop-cpd/data/'
MYFILE = PATH + 'german_credit_data.csv'
NEWFILE = PATH + 'new_german.csv'

print('Writing data with pre-pended uuid to ' + NEWFILE + '...')

try:
    f = open(MYFILE, 'r+')
    new_german = open(NEWFILE, 'w')

    for line in f.readlines():
        id = uuid.uuid4()
        add_line = (str(id) + ',' + line)
        new_german.write(add_line)
finally:
    if f:
        f.close()
    if new_german:
        new_german.close()
