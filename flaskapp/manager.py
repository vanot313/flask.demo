# coding:utf-8
from application import app, manager
from flask_script import Server, Command

from www import *



# create_table
@Command
def create_all():
    from application import db
    from common.models.user import User
    db.create_all()


# 添加shell命令控制
manager.add_command("runserver", Server(use_debugger=True, use_reloader=True, host='0.0.0.0'))
manager.add_command("create_all", create_all)


# 被调用的实际主函数
def main():
    # 启动manager的shell命令控制
    manager.run()


if __name__ == "__main__":
    try:
        import sys
        # 执行该文件后，调用main
        sys.exit(main())

    except Exception as e:
        import traceback
        traceback.print_exc()
