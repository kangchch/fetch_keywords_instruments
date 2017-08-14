# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient
import datetime

mongo_db_Conn = pymongo.MongoClient('192.168.60.65', 10010).medical_instruments

db_medical = mongo_db_Conn.medical_instruments_import_tbl

for i in xrange(1, 3200):
    db_medical.insert({'keywords': '', 'status': 0, 'page': i, 'insert_time': datetime.datetime.now()})
