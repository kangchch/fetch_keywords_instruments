
from pymongo import MongoClient
import datetime
import re
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':

    fp_medical = open('medical_china.csv', 'wb')
    mongo_db = MongoClient('192.168.60.65', 10010).medical_instruments
    mongo_db_tbl = mongo_db.medical_instruments_tbl

    all_keywords = [keywords['keywords'] for keywords in mongo_db_tbl.find({})]




    fp_medical.close()

