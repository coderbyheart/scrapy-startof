# Scrapy settings for startof project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

# BOT_NAME = 'startof'
# BOT_VERSION = '1.0'

BOT_NAME = 'curl'
BOT_VERSION = '7.29.0'

SPIDER_MODULES = ['startof.spiders']
NEWSPIDER_MODULE = 'startof.spiders'
DEFAULT_ITEM_CLASS = 'startof.items.StartofItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['startof.pipelines.StartofPipeline']