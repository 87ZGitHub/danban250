import scrapy
from douban250.items import Douban250Item

class Douban250Spider(scrapy.Spider):
    name = "douban250"

    start_urls = ['https://movie.douban.com/top250']

    url = 'http://movie.douban.com/top250'

    def parse(self, response):

        item = Douban250Item()
        Movies = response.xpath('//div[@class="item"]')
        for eachMovie in Movies:
            rank = eachMovie.xpath('div[@class="pic"]/em/text()').extract()
            #pic = eachMovie.xpath('div[@class="pic"/a/img/@src')
            title = eachMovie.xpath('div[@class="info"]/div[@class="hd"]/a/span/text()').extract()
            fullTitle = ''
            for eachTitle in title:
                fullTitle += eachTitle
            info = eachMovie.xpath('div[@class="info"]/div[@class="bd"]/p/text()').extract()
            rating = eachMovie.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/text()').extract()[0]
            critical = eachMovie.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/text()').extract()[1]
            quote = eachMovie.xpath('p[@class="quote"]/span/text()').extract()
            if quote:
                quote = quote[0]
            else:
                quote = ''
            item['rank'] = rank
            item['title'] = fullTitle
            item['info'] = ';'.join(info)
            item['rating'] = rating
            item['critical'] = critical
            item['quote'] = quote
            yield item
        nextLink = response.xpath('//span[@class="next"]/link/@href').extract()
        if nextLink:
            nextLink = nextLink[0]
            print nextLink
            yield scrapy.Request(self.url + nextLink, callback=self.parse)

