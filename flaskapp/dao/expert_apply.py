from common.models.expert_apply import ExpertApply
from application import db


class ExpertApplyDao:
    def getByApplyId(self, apply_id):
        result = ExpertApply.query.filter(ExpertApply.apply_id == int(apply_id))
        return result

    def getByUserId(self, user_id):
        result = ExpertApply.query.filter(ExpertApply.user_id == int(user_id))
        return result

    def getByName(self, name):
        result = ExpertApply.query.filter(ExpertApply.username == name)
        return result

    def getAll(self, page="1", per_page="10"):
        if page is None:
            page = 1
        if per_page is None:
            per_page = 10

        result = ExpertApply.query.filter(ExpertApply.status == 0)

        result = result.paginate(page=int(page), per_page=int(per_page))
        ans = {'data': result.items, 'pages': result.pages, 'total': result.total}
        return ans

    def update(self, entity):
        result = ExpertApply.query.filter(ExpertApply.apply_id == int(entity.apply_id)).first()
        result = entity
        db.session.commit()
        return result

    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity
