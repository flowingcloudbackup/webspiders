# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_test project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'webspiders'

SPIDER_MODULES = ['webspiders.spiders']
NEWSPIDER_MODULE = 'webspiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'scrapy_test (+http://www.yourdomain.com)'weibo_spider

DOWNLOAD_DELAY = 10
TIME_DELAY = 30

# Pipelines config
ITEM_PIPELINES = {'webspiders.pipelines.ScrapyWeiboPipeline': 300}

# 处理js的中间间
DOWNLOAD_MIDDLEWARES = {
    'scrapyjs.SplashMiddleware': 725,
}

# MySql configuration
MYSQL_HOST = "localhost"
USER_NAME = "root"
PASSWORD = "whq"
DATABASE = "webspider"
SQL_PATH = '/home/haiqw/Documents/my_projects/webspiders/webspiders/mysql.cfg'

# logging config
