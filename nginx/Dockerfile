FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/

COPY app/dist /usr/share/nginx/html
COPY app/admin /usr/share/nginx/html/admin

# RUN /etc/init.d/nginx start