# -*- coding: utf-8 -*-

from pymongo import MongoClient

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MongoDBPipeline(object):

    def __init__(self):
        self.conn = MongoClient("172.17.0.1", 27017)
        self.db = self.conn["spider"]
        self.collection = self.db["scrapy_dealer_redis"]

    def process_item(self, item, spider):
        self.collection.insert_one(item)
        return item

    def close_spider(self, spider):
        self.conn.close()
