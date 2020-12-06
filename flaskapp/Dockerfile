FROM python:3.4
MAINTAINER 2834552723@qq.com

RUN mkdir /app
WORKDIR /app

ADD . /app
RUN pip install -r requirements.txt && pip install uwsgi

CMD["uwsig","--ini","uwsgi.ini"]
