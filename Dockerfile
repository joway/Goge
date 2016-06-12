FROM python:3.5.1
MAINTAINER Joway Wong "joway.w@gmail.com"

# Install packages
RUN apt-get update && apt-get install -y \
    git \
    libmysqlclient-dev \
    mysql-client \
    nginx \
    supervisor

RUN mkdir /goge
WORKDIR /goge

# Configure Nginx and uwsgi
ADD ./requirements.txt /goge/requirements.txt
RUN rm /etc/nginx/sites-enabled/default
ADD ./.deploy/nginx.conf /etc/nginx/sites-enabled/goge.conf

# supervisord
ADD ./.deploy/uwsgi_nginx_supervisord.conf /etc/supervisor/conf.d/
ADD ./.deploy/celery_supervisord.conf /etc/supervisor/conf.d/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

ADD . /goge

EXPOSE 80
CMD ["supervisord", "-n"]


