import sys
import os
import time
import argparse
#import pandas as pd
import json
import pymongo

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

MONGODB_UNAME = 'root' #'admin'
MONGODB_PWD = 'ENTER_YOUR_PASSWORD'
MONGODB_HNAME = 'MONGODB_IP_ADDRESS'
MONGODB_PORT = '27017'
MONGODB_CERT_FILE = '/Users/PATH_TO_CERT.crt'


def upload_content(datafilepath, mng_dbname, mng_collname):
    #client = MongoClient(
    #    "mongodb://{}:{}@{}:{}/ibmclouddb?authSource=admin&replicaSet=replset".format(MONGODB_UNAME,MONGODB_PWD,MONGODB_HNAME,MONGODB_PORT),
    #    ssl=True,
    #    ssl_ca_certs=MONGODB_CERT_FILE
    #)
    client = MongoClient(
        "mongodb://{}:{}@{}:{}/".format(MONGODB_UNAME,MONGODB_PWD,MONGODB_HNAME,MONGODB_PORT)
    )

    db = client[mng_dbname]
    db_cm = db[mng_collname]
    data = pd.read_csv(datafilepath)
    data_json = json.loads(data.to_json(orient='records'))
    print("Number of documents: ",len(data_json))
    
    db_cm.delete_many({})
    updateddocs = []
    for doc in data_json:
        #If you want to use the CUSTOMERID as the document ID, uncomment the following line.
        #doc['_id'] = doc.pop('CUSTOMERID')
        updateddocs.append(doc)
    
    print(json.dumps(updateddocs, indent=2))
    db_cm.insert_many(updateddocs)

if __name__ == "__main__":
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or higher version is required for this script.")

    parser = argparse.ArgumentParser(prog="python %s)" % os.path.basename(__file__), description='Script that uploads documents to a mongodb collection')
    parser.add_argument('-data-csv-file', dest='data_csv', required=True, help='Load Data CSV File')
    parser.add_argument('-db-name', dest='db_name', required=True, help='Mongo DB Name')
    parser.add_argument('-collection-name', dest='coll_name', required=True, help='Mongo Collection Name')

    args = parser.parse_args()
    started_time = time.time()
    print("Starting file upload script......")
    upload_content(args.data_csv, args.db_name, args.coll_name)
    elapsed = time.time() - started_time
    print("Finished file upload script. Elapsed time: %f" % elapsed)
