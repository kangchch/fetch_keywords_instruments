# -*- coding: utf-8 -*-

import requests
import pymongo
import time
import datetime
import os
import logging
import re

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

sys.path.append('/tools/python_common')
from common_func import logInit


def getpage_Mongodb(mongodbConn):
    result = []
    if not mongodbConn:
        return None
    db = mongodbConn.medical_instruments
    collection = db.medical_instruments_import_tbl
    ret = collection.find({'status': 0}, {'page': 1})
    [result.append(con['page']) for con in ret if con['page']]
    return result

def update_Mongodb(mongodbConn, page, keywords, status):
    db = mongodbConn.medical_instruments
    collection = db.medical_instruments_import_tbl
    collection.update(
            {'page': page},
            {'$set':
                {
                    'keywords': keywords,
                    'status': status,
                    'update_time': datetime.datetime.now()
                }
            }
                    )
def fetch_instruments(page):

    curstart = page
    post_values = {
            'tableId': '27',
            'State': '1',
            'bcId': '118103063506935484150101953610',
            'State': '1',
            'curstart': str(curstart),
            'State': '1',
            'tableName': 'TABLE27',
            'State': '1',
            'viewtitleName': 'COLUMN200',
            'State': '1',
            'viewsubTitleName': 'COLUMN199, COLUMN192',
            'State': '1',
            'tableView': '%E8%BF%9B%E5%8F%A3%E5%99%A8%E6%A2%B0',
            'State': '1',
    }
    post_headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        # 'Connection': 'keep-alive',
        'cache-control': 'no-cache',
        'Accept-Encoding': 'gzip,deflate',
    }
    url = 'http://app1.sfda.gov.cn/datasearch/face3/search.jsp'
    counter = 0
    while counter < 3:
        try:
            response = requests.post(url, data = post_values, headers = post_headers, timeout = 5)
            logging.info('-----response_status_code is      %d : -----' % response.status_code)
            resHtml = response.text
        except requests.exceptions.RequestException as e:
            counter += 1
            logging.error('%s, counter = %d' % (str(e), counter))
        else:
            # update_Mongodb(mongodbConn, curstart, '', 0)
            return resHtml


if __name__ == '__main__':

    DIR_PATH = os.path.split(os.path.realpath(__file__))[0]
    LOG_FILE = DIR_PATH + '/logs/' + __file__.replace('.py', '.log')
    logInit(logging.INFO, LOG_FILE, 0, True)

    mongodbConn = pymongo.MongoClient('192.168.60.65', 10010)
    pages = getpage_Mongodb(mongodbConn)
    for page in pages:
        time.sleep(2)
        response = fetch_instruments(page)
        if not response:
            logging.error('fetch failed! failed page = %d' % (page))
            update_Mongodb(mongodbConn, page, '', 0)
        else:
            keywords = r'(?=\d+\.).*(?= 国)'
            sites = re.findall(keywords, response)
            if 0 == len(sites):
                update_Mongodb(mongodbConn, page, '', 0)
                logging.info('update_Mongodb page = %d , status = 0, update_time = %s' % (page, datetime.datetime.now()))
            else:
                update_Mongodb(mongodbConn, page, sites, 1)
                logging.info('update_Mongodb page = %d , status = 1, update_time = %s' % (page, datetime.datetime.now()))

