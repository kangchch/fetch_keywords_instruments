# -*- coding: utf-8 -*-

import requests
import time
import datetime
import os
import re
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def fetch_instruments(num):

    curstart = num
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
            'viewsubTitleName': 'COLUMN199,COLUMN192',
            'State': '1',
            'tableView': '%E8%BF%9B%E5%8F%A3%E5%99%A8%E6%A2%B0',
            'State': '1',
    }
    post_headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Connection': 'keep-alive',
        'cache-control': 'no-cache',
        'Accept-Encoding': 'gzip,deflate',
    }
    url = 'http://app1.sfda.gov.cn/datasearch/face3/search.jsp'
    response = requests.post(url, data = post_values, headers = post_headers)
    resHtml = response.text

    print ('-----status code    is %d : -----'  % response.status_code)
    print ('-----current page   is %d : -----' % curstart)

    res = resHtml.encode('utf-8')
    keywords = r'(?=\d+\.).*(?= 国)'
    sites = re.findall(keywords, res)

    length = len(sites)
    print ('-----keywords count is %d : -----' % length)

    for site in sites:
        print site.decode('utf-8')

if __name__ == '__main__':

    fetch_instruments(44)

