from operator import *

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

    def getFuzzy(self, status="", page="1", per_page="10", apply_id=""):
        if page is None:
            page = 1
        if per_page is None:
            per_page = 10
        if status is None:
            status = '0'
        if apply_id is None:
            apply_id = ''

        if apply_id is not "":
            key1 = ExpertApply.user_id.like("%" + str(apply_id) + "%")
        # if order_id is not "":
        #     key2 = ExpertApply.order_id.like("%" + str(order_id) + "%")
        # if expert_id is not "":
        #     key3 = ExpertApply.expert_id.like("%" + str(expert_id) + "%")
        if status is not "":
            key4 = ExpertApply.status.like("%" + str(status) + "%")

        key1 = or_(ExpertApply.apply_id.like("%" + str(apply_id) + "%"), ExpertApply.apply_id.is_(None))
        key4 = or_(ExpertApply.status.like("%" + str(status) + "%"), ExpertApply.status.is_(None))

        result = ExpertApply.query.order_by(ExpertApply.create_time.desc()).filter(
            and_(
                key1,
                # key2,
                # key3,
                key4
            )
        )

        result = result.paginate(page=int(page), per_page=int(per_page))
        ans = {}
        ans['data'] = result.items
        ans['pages'] = result.pages
        ans['total'] = result.total

        return ans



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
