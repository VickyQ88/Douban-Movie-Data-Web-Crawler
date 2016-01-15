import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class MongoPipeline(object):

    # collection_name = 'scrapy_items'

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]        
    
    # def from_crawler(cls, crawler):
    #     return cls(
    #         mongo_uri=crawler.settings.get('MONGO_URI'),
    #         mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
    #     )

    # def open_spider(self, spider):
    #     self.client = pymongo.MongoClient(self.mongo_uri)
    #     self.db = self.client[self.mongo_db]

    # def close_spider(self, spider):
    #     self.client.close()

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item