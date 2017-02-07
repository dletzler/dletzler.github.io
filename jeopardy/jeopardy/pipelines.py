# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WriteItemPipeline(object):
    def __init__(self):
        self.filename = 'Jeopardy.txt'

    def open_spider(self, spider):
        self.file = open(self.filename, 'wb')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = str(item['Round']) + '\t' + str(item['Category']) + '\t' + str(item['Value']) + '\t' + str(item['Clue']) + '\t' + str(item['Answer'])\
         + '\t' + str(item['Order'])  + '\t' + str(item['Right']) + '\n'
        self.file.write(line)
        return item
