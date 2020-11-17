# coding:utf-8
from application import app, manager
from flask_script import Server, Command
from www import *

# web server
manager.add_command("runserver", Server(use_debugger=True, use_reloader=True, host='0.0.0.0'))


# create_table
@Command
def create_all():
    from application import db
    from common.models.user import User
    db.create_all()


manager.add_command("create_all", create_all)


def main():
    manager.run()


if __name__ == "__main__":
    try:
        # 这里是干嘛的
        import sys
        sys.exit(main())

    except Exception as e:
        import traceback
        traceback.print_exc()