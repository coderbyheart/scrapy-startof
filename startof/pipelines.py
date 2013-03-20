import os

class StartofPipeline(object):
    def process_item(self, item, spider):
        print '"%s" <%s>' % (item['name'], item['email'])
        return item
