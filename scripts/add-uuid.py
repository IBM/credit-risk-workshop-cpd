#!/usr/bin/env python

import uuid

PATH = '/Users/scott/gitRepos/Sandbox/credit-risk-workshop-cpd/data/'
MYFILE = PATH + 'german_credit_data.csv'
NEWFILE = PATH + 'new_test.csv'

print('Writing data with pre-pended uuid to ' + NEWFILE + '...')

with open(MYFILE, 'r+') as f:
    with open(NEWFILE, 'w') as new_german:
        for line in f:
            id = uuid.uuid4()
            add_line = (str(id) + ',' + line)
            new_german.write(add_line)
