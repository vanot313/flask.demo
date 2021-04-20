FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/

COPY app/user /usr/share/nginx/html
# COPY app/user /usr/share/nginx/user
COPY app/admin /usr/share/nginx/admin
COPY app/expert /usr/share/nginx/expert

# RUN /etc/init.d/nginx start