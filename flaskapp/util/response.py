from flask import jsonify


# 返回到前端json数据格式
def response(msg, code, data):
    result = {'msg': msg, 'code': code, 'data': serialize(data), 'success': (code == 200)}
    return jsonify(result)


# 序列化数据
def serialize(model):
    from sqlalchemy.orm import class_mapper
    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, getattr(model, c)) for c in columns)
