FROM python:3.4
MAINTAINER 2834552723@qq.com

RUN mkdir /app
WORKDIR /app

ADD . /app

RUN pip install -i https://pypi.doubanio.com/simple/  --trusted-host pypi.doubanio.com -r requirements.txt && pip install uwsgi -i https://pypi.doubanio.com/simple/  --trusted-host pypi.doubanio.com

CMD ["uwsgi","--ini","uwsgi.ini"]
