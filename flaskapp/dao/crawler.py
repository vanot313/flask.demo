from common.models.crawler import Crawler
from application import db


class CrawlerDao:
    def getById(self, id):
        result = Crawler.query.filter(Crawler.id == id)
        return result

    def getByName(self, name):
        result = Crawler.query.filter(Crawler.name == name).first()
        return result

    def update(self, entity):
        result = Crawler.query.filter(Crawler.id == entity.id).first()
        result = entity
        db.session.commit()
        return result

    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, id):
        result = Crawler.query.filter(Crawler.id == int(id)).first()
        result.status = 1
        return self.update(result)

    def getAll(self):
        result = Crawler.query.all()
        return result
