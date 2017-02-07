from scrapy import Spider
from scrapy import Selector
from bs4 import BeautifulSoup
from jeopardy.items import JeopardyItem

class JeopardySpider(Spider):
    name = "jeopardy_spider"
    allowed_urls = ["http://www.j-archive.com/"]
    start_urls = ["http://www.j-archive.com/showgame.php?game_id=5512"]


#    def parse(self, response):
#        page_urls = [rep("", max)]
#        for i in range(1, ):
#            page_urls[i] = ["http://www.j-archive.com/showgame.php?game_id=" + str(i)
#        for page_url in page_urls:
#            yield scrapy.Request(page_url, callback=self.parse_game)


    def parse(self, response):

        first_round = response.xpath('//*[@id="jeopardy_round"]/table[1]/tr').extract()
        i = 0
        while i <1:
            Round = "First"
            Category = "".join([x.encode('UTF-8') for x in Selector(text=first_round[0]).xpath('//*/td[1]/table/tr[1]/td/text()').extract()[0]])
            Value = "".join([x.encode('UTF-8') for x in Selector(text=first_round[1]).xpath('//*/td[1]/table/tr[1]/td/div/table/tr/td[2]/text()').extract()[0]])
            Clue = "".join([x.encode('UTF-8') for x in Selector(text=first_round[1]).xpath('//*/td[1]/table/tr[2]/td/text()').extract()[0]])
            Answer = BeautifulSoup("".join([x.encode('UTF-8') for x in Selector(text=first_round[1]).xpath('//*/td[1]/table/tr[1]/td/div/@onmouseover').extract()[0]]), "lxml").find('em', {'class':'correct_response'}).get_text()
            Order = "".join([x.encode('UTF-8') for x in Selector(text=first_round[1]).xpath('//*/td[1]/table/tr[1]/td/div/table/tr/td[3]/a/text()').extract()[0]])
            Right = BeautifulSoup("".join([x.encode('UTF-8') for x in Selector(text=first_round[1]).xpath('//*/td[1]/table/tr[1]/td/div/@onmouseover').extract()[0]]), "lxml").find('td', {'class':'right'}).get_text()


            item = JeopardyItem()
            item['Round'] = Round
            item['Category'] = Category
            item['Value'] = Value
            item['Clue'] = Clue
            item['Answer'] = Answer
            item['Order'] = Order
            item['Right'] = Right
            i+= 1
            yield item
