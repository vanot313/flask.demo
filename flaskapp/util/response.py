from flask import jsonify


# 返回到前端json数据格式
def response(msg, code, data):
    if not data:
        result = {'msg': msg, 'code': code, 'success': (code == 200)}
    else:
        result = {'msg': msg, 'code': code, 'data': serialize(data), 'success': (code == 200)}
    return jsonify(result)


def response_multiple(msg, code, data):
    if not data:
        result = {'msg': msg, 'code': code, 'success': (code == 200)}
    else:
        result = {'msg': msg, 'code': code, 'data': serialize_multiple(data), 'success': (code == 200)}
    return jsonify(result)


def response_dict(msg, code, data):
    if not data:
        result = {'msg': msg, 'code': code, 'success': (code == 200)}
    else:
        res = {}
        for i in data:
            res[i] = serialize(data[i])
        result = {'msg': msg, 'code': code, 'data': res, 'success': (code == 200)}
    return jsonify(result)


# 序列化单个数据
def serialize(model):
    from sqlalchemy.orm import class_mapper
    columns = [c.key for c in class_mapper(model.__class__).columns]

    return dict((c, str(getattr(model, c))) for c in columns)


# 序列化批量数据
def serialize_multiple(models):
    tuple = []
    for model in models:
        from sqlalchemy.orm import class_mapper
        columns = [c.key for c in class_mapper(model.__class__).columns]
        tuple.append(dict((c, str(getattr(model, c))) for c in columns))
    return tuple

# code 含义
# 200 成功
# 1001 查询失败
# 1002
