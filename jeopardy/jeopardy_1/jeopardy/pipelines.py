# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class WriteItemPipeline(object):
    def __init__(self):
        self.filename = "Jeopardy.csv"

    def open_spider(self, spider):
        self.csvfile = open(self.filename, 'wb')
        self.exporter = CsvItemExporter(self.csvfile)
        self.exporter.start_exporting()

    def close_spder(self, spider):
        self.exporter.finish_exporting()
        self.csvfile.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

#class WriteItemPipeline(object):
#    def __init__(self):
#        self.filename = 'Jeopardy.txt'
#
#    def open_spider(self, spider):
#        self.file = open(self.filename, 'wb')
#
#    def close_spider(self, spider):
#        self.file.close()
#
#    def process_item(self, item, spider):
#        line = '\n' + str(item['Episode']) + '\t'+ str(item['Date']) + '\t' + '\t'+ str(item['Round'])\
#         + '\t' + str(item['Category']) + '\t' + str(item['Value']) + '\t' + str(item['Clue']) + '\t' + str(item['Answer'])\
#         + '\t' + str(item['Order'])  + '\t' + str(item['DailyDouble']) + str(item['Right']) + '\t' + '\t' + str(item['Wrong1'])\
#         + '\t' + str(item['Wrong2']) + '\t' + str(item['Wrong3']) + '\t' + str(item['Wrong4']) + "\n"
#        self.file.write(line)
#        return item
