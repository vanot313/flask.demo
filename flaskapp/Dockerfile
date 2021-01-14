FROM python:3.6
MAINTAINER 2834552723@qq.com

RUN mkdir /flaskapp
WORKDIR /flaskapp

ADD . /flaskapp

RUN pip install -i https://pypi.doubanio.com/simple/  --trusted-host pypi.doubanio.com -r requirements.txt && pip install uwsgi -i https://pypi.doubanio.com/simple/  --trusted-host pypi.doubanio.com

CMD ["uwsgi","--ini","uwsgi.ini"]
