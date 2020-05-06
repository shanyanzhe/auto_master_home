# -*- coding: utf-8 -*-

# Scrapy settings for auto_master_home project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'auto_master_home'

SPIDER_MODULES = ['auto_master_home.spiders']
NEWSPIDER_MODULE = 'auto_master_home.spiders'

# Close spider
custom_settings = {
    "CLOSESPIDER_TIMEOUT": 3600
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"

# Redis连接池
REDIS_URL = "redis://:123456@172.17.0.1:6379/1"
#REDIS_URL = "redis://:Gunlei@spider@47.94.196.79:6377/1"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 1

# Log Setting
LOG_LEVEL = 'DEBUG'

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}


# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'auto_master_home.middlewares.ProxyMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#IDLE_TIME = 60
#EXTENSIONS = {
#    'scrapy_redis_extension.RedisSpiderClosedExensions': 500
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'auto_master_home.pipelines.MongoDBPipeline': 300,
    #'scrapy_redis.pipelines.RedisPipeline': 400,
}

