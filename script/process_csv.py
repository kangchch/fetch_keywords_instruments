
# coding:utf-8
import csv
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

csvfile = codecs.open('import_1.csv', 'rb', 'utf-8')
reader = csv.reader(csvfile)

csvfile_w = codecs.open('export.csv', 'wb', 'utf-8')
writer = csv.writer(csvfile_w)

for index, line in enumerate(reader):
    if index == 0 or not line:
        continue
    s = line[0].decode('utf-8', 'ignore')
    pos = s.rfind(u' (')
    writer.writerow((s[:pos], s[pos+2:]))


