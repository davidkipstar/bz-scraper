from __future__ import absolute_import
import scrapy

from scrapy.loader import ItemLoader
from bzscrapy.items import BzArtilce,BzBlock

def parse(self, response):
    l = ItemLoader(item=Product(), response=response)
class BZSpider(scrapy.Spider):
    name = "BZSpider"
    def start_requests(self):
        urls = ['https://www.bz-berlin.de/',
                'https://www.bz-berlin.de/berlin',
                'https://www.bz-berlin.de/thema/bezirke',
                'https://www.bz-berlin.de/tatort',
                'https://www.bz-berlin.de/sport',
                'https://www.bz-berlin.de/thema/kultur-und-leute',
                'https://www.bz-berlin.de/thema/nachrichten',
                'https://www.bz-berlin.de/erotik']
        #
        for url in urls:
            #
            yield scrapy.Request(url=url, callback=self.parse_section,errback=self.errback_bz)

    def parse_section(self, response):
        #get all blocks of articles 
        pages = response.url.split("/")
        page = pages[-2]

        xpath2section = '/html/body/section[contains(@class,"pagerender")]'

        xpath2articles= '//div/div/div/div/div/a[contains(@href,"bz-berlin")]'

        xpath2category = '//div/div/header/h2/a/@href'
        xpath2img = '//div/a/figure/img' # u'<img data-original="https://www.bz-berlin.de/data/uploads/2017/08/13245095_1503909344-480x270.jpg" alt="Der Preis f\xfcr Butter hat sich binnen eines Jahres verdoppelt. Unklar ist, ob sich die Kosten wieder einpendeln." src="https://www.bz-berlin.de/data/img/placeholder-bz-teaser-a-704x396.png" class="js-lazyload">',
        
        #response.xpath('/html/body/section[contains(@class,"pagerender")]/div/div/div/div/div/div/a')
        sections = response.xpath(xpath2section)
        for idx,section in enumerate(sections):
            Item = ItemLoader(item=BzBlock(), response=response)#load item
            img = section.xpath(xpath2img)
            category = section.xpath(xpath2category)
            articles = section.xpath(xpath2articles)

            Item['origin'] = response.url
            #write data to item
            Item['articles'] = dict(enumerate(articles)) 
            #if(article.xpath(xpath2category).extract()):
            Item['category'] = article.xpath(xpath2category).extract()
            #else:
            yield Item
            for article in articles:
                yield scrapy.Request(url=article.xpath('@href').extract(),callback=self.parse_article,errback=errback_bz)
    def parse_article(self,response):
        # - create article Item
        # emotions missing, and img+ description
        #    url = scrapy.Field()
        #author = scrapy.Field()
        #categories = scrapy.Field()
        #date = scrapy.Field()
        #emotions = scrapy.Field()
        #title = scrapy.Field()
        #headline = scrapy.Field()
        #text = scrapy.Field()
        article = ItemLoader(item=BzArtilce(), response=response)
        #xpath 
        xpath2headline = '/html/body/div[4]/article/header/div[1]' #h2 is thema,h1 is headline
        xpath2header = '/html/body/div[4]/article/div[1]/div[2]/section/div/header'
        xpath2article = '/html/body/div[4]/article/div[1]/div[2]/section/div/p'

        xpath2author = '//div[1]/author/span[2]'
        xpath2date = '//div[2]/time/'
        xpath2categories = '//div[2]/div/div[2]/ul'
        xpath2thema = '//div[2]/div/div[1]/ul'
        
        #select data 
        headline = response.xpath(xpath2headline)
        header = response.xpath(xpath2header)
        article = response.xpath(xpath2article)

        categories = header.xpath(xpath2categories)
        thema = header.xpath(xpath2thema)
        date = header.xpath(xpath2date)
        author = header.xpath(xpath2author)

        #assign fields
        article['url'] = response.url
        article['categories'] = header.xpath('li').extract()
        article['date'] = date.extract()
        article['title'] = header.xpath('@h1').extract_first()
        article['headline'] = header.xpath('@h1').extract_first()
        article['text'] = article.extract()
        print('article created !219340148190218419038290*#@()')
        return article


    def errback_bz(self,failure):
                # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)
        #