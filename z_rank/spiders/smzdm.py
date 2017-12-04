# -*- coding: utf-8 -*-
import scrapy


class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['m.smzdm.com']
    start_urls = ['http://m.smzdm.com/']

    def parse(self, response):
        self.log('response:')
        list = response.css('#wrapper .card-group-list')
        for item in list:
            self.log('title: %s' % item.css('.zm-card-title::text').extract_first())
            price = item.css('.card-price::text').extract_first()
            self.log('price: %s' % ( price if price is None else price.strip()))
            self.log('mall: %s' % item.css('.card-mall::text').extract_first())
            self.log('posted_at: %s' % item.css('.zm-card-actions-left span span:not(.card-mall)::text').extract_first())
            gt_texts = item.css('.zm-card-actions-right .icon-group::text')
            self.log('comments_count: %s' % gt_texts[1].extract())
            self.log('vote_percent %s' % gt_texts[3].extract())
