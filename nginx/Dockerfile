FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/

COPY app/dist /usr/share/nginx/html

RUN /etc/init.d/nginx start