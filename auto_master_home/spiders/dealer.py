# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.http import Request
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
import datetime


class DealerSpider(RedisCrawlSpider):
    name = 'dealer'
    allowed_domains = ['16888.com']
    redis_key = "dealer:start_urls"

    rules = (
        Rule(LinkExtractor(allow=r'\/\?tag=search&pid=\d+$'), follow=True),
        Rule(LinkExtractor(allow=r'\/\?tag=search&pid=\d+&cid=\d+$'), follow=True),
        Rule(LinkExtractor(allow=r'\/\?tag=search&pid=\d+&cid=\d+&page=\d+'),
             callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):
        self.logger.info("Hi, this is an item page! %s", response.url)
        dealer_list = response.css(".dealer-list")
        for dealer in dealer_list:
            item = {}
            dealer_name = dealer.css(".dealer-text .title").xpath("./a/text()").getall()
            dealer_type = dealer.css(".dealer-text .title").xpath("./b/text()").getall()
            dealer_major = dealer.css(".dealer-text .camp").xpath("./p/a/text()").getall()
            dealer_phone = dealer.css(".dealer-text .camp").xpath("./em/text()").getall()
            dealer_address = dealer.css(".dealer-text .camp").xpath("./p/text()").getall()
            dealer_city = dealer.css(".dealer-city").xpath("./p/text()").getall()
            item["dealer_name"] = dealer_name[0] if len(dealer_name) > 0 else None
            item["dealer_type"] = dealer_type[0] if len(dealer_type) > 0 else None
            item["dealer_phone"] = dealer_phone[0] if len(dealer_phone) > 0 else None
            item["dealer_major"] = ",".join(dealer_major[0: -1]) if len(dealer_major) > 0 else None
            item["dealer_address"] = "".join(dealer_address).replace("\n", "").replace(" ", "") if len(dealer_address) > 0 else None
            item["dealer_city"] = dealer_city[0] if len(dealer_city) > 0 else None
            item["dealer_area"] = dealer_city[1] if len(dealer_city) > 1 else None
            item["crawl_datetime"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            yield item

