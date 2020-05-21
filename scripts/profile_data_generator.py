import csv
from faker import Faker
import datetime
import random
import sys
import os
import time
import argparse
import pandas as pd
import json
import uuid

PROFILE_FIELD_NAMES = ("CUSTOMERID","FIRSTNAME","LASTNAME","EMAIL","STREETADDRESS","CITY","STATE","POSTALCODE")


def generate_profile(profile_locale, records, output_file_name):
    fake = Faker(profile_locale)
    profile_data = []
    for i in range(records):
        p = {}
        t_fname = fake.first_name()
        t_lname = fake.last_name()
        t_email = t_fname[:1] + t_lname + str(random.randint(1,100)) + '@' + random.choice([fake.domain_name(), fake.free_email_domain()])
        p['CUSTOMERID'] =  uuid.uuid4()
        p['FIRSTNAME'] = t_fname
        p['LASTNAME'] = t_lname
        p['EMAIL'] = t_email #fake.email()
        p['STREETADDRESS'] = fake.street_address()
        p['CITY'] = fake.city()
        p['STATE'] = fake.state_abbr()
        p['POSTALCODE'] = fake.postcode_in_state(p['STATE'])#fake.zipcode()
        profile_data.append(p)

    try:
        with open(output_file_name, 'w') as out_csv_file:
            writer = csv.DictWriter(out_csv_file, fieldnames=PROFILE_FIELD_NAMES)
            writer.writeheader()
            for data in profile_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")

def generate_credit_risk_profile(profile_locale, input_file_name, output_file_name):
    fake = Faker(profile_locale)
    all_field_names = ("CUSTOMERID","CHECKINGSTATUS","LOANDURATION","CREDITHISTORY","LOANPURPOSE","LOANAMOUNT","EXISTINGSAVINGS","EMPLOYMENTDURATION","INSTALLMENTPERCENT","SEX","OTHERSONLOAN","CURRENTRESIDENCEDURATION","OWNSPROPERTY","AGE","INSTALLMENTPLANS","HOUSING","EXISTINGCREDITSCOUNT","JOB","DEPENDENTS","TELEPHONE","FOREIGNWORKER","RISK")
    profile_data = []
    with open(input_file_name, 'r') as csv_file:
        next(csv_file, None)
        print('Reading in the CSV from input file: %s' % csv_file)
        reader = csv.DictReader(csv_file , fieldnames = all_field_names)
        for row in reader:
            p = {}
            t_fname = ''
            if(row["SEX"].lower() == "female"):
                #Generate Female 
                t_fname = fake.first_name_female()
            elif(row["SEX"].lower() == "male"):
                #Generate Male
                t_fname = fake.first_name_male()
            else:
                sys.exit("Error with dataset gender.")

            t_lname = fake.last_name()
            t_email = t_fname[:1] + t_lname + str(random.randint(1,100)) + '@' + random.choice([fake.domain_name(), fake.free_email_domain()])
            p['CUSTOMERID'] = row["CUSTOMERID"]
            p['FIRSTNAME'] = t_fname
            p['LASTNAME'] = t_lname
            p['EMAIL'] = t_email 
            p['STREETADDRESS'] = fake.street_address()
            p['CITY'] = fake.city()
            p['STATE'] = fake.state_abbr()#fake.state()
            p['POSTALCODE'] = fake.postcode_in_state(p['STATE'])#fake.zipcode()
            profile_data.append(p)

    try:
        with open(output_file_name, 'w') as out_csv_file:
            writer = csv.DictWriter(out_csv_file, fieldnames=PROFILE_FIELD_NAMES)
            writer.writeheader()
            for data in profile_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")


if __name__ == "__main__":
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or higher version is required for this script.")

    parser = argparse.ArgumentParser(prog="python %s)" % os.path.basename(__file__), description='Script that generates fake profile data for german credit data set using Faker library')
    parser.add_argument('-output-file-name', dest='output_fname', required=True, help='CSV File Name where data will be stored.')
    parser.add_argument('-german-credit-file-name', dest='orig_fname', required=False, default=None, help='CSV File with german credit data set.')
    parser.add_argument('-profile-locale', dest='plocale', required=False, default='en_US', help='Locale used to generate data.')
    parser.add_argument('-record-count', dest='num_records', required=False, type=int, default=0, help='Mongo Collection Name')

    print("Starting profile generation script......")
    args = parser.parse_args()
    started_time = time.time()

    if args.orig_fname is not None:
        # Do german credit data set profile
        #orig_fname = '/Users/jrtorres/Desktop/german_credit_data.csv'
        #output_fname = '/Users/jrtorres/Desktop/profile_data.csv'
        generate_credit_risk_profile(args.plocale, args.orig_fname, args.output_fname)
    elif args.num_records > 0:
        # Do generic profile
        generate_profile(args.plocale, args.num_records, args.output_fname)
    else:
        print("Invalid parameters. Supply either german credit risk data file or number of records to generate.")

    elapsed = time.time() - started_time
    print("Finished profile generation script. Elapsed time: %f" % elapsed)


