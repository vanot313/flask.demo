from application import db


class admin(db.Model):
    __tablename__ = 't_admin'

    id = db.Column(db.BIGINT, primary_key=True)
    username = db.Column(db.String(50))
    _password_ = db.Column(db.String(128))
    email = db.Column(db.String(128))
    mobile = db.Column(db.String(20))
    status = db.Column(db.CHAR(1))
    create_time = db.Column(db.DATETIME)
    modify_time = db.Column(db.DATETIME)
    last_login_time = db.Column(db.DATETIME)
    avatar = db.Column(db.String(100))
    description = db.Column(db.String(100))