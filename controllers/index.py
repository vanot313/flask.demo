from flask import Blueprint, render_template
from common.models.user import User
from common.models.account import Account

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index():
    context = {}
    # result = User.query.all()
    result = Account.query.all()
    context['result'] = result
    return render_template("index.html", **context)