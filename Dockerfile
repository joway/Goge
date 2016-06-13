FROM python:3.5.1
MAINTAINER Joway Wong "joway.w@gmail.com"

# Install packages
RUN apt-get update && apt-get install -y \
    git \
    libmysqlclient-dev \
    mysql-client \
    nginx \
    supervisor

RUN mkdir /goge /var/log/celery
WORKDIR /goge
# for celery log files
RUN touch /var/log/celery/goge_worker.log \
    /var/log/celery/goge_beat.log

VOLUME /var/log

# Configure Nginx and uwsgi
ADD ./requirements.txt /goge/requirements.txt
RUN rm /etc/nginx/sites-enabled/default
ADD ./.deploy/nginx.conf /etc/nginx/sites-enabled/goge.conf

# supervisord
ADD ./.deploy/uwsgi_nginx_supervisord.conf /etc/supervisor/conf.d/
ADD ./.deploy/celery_supervisord.conf /etc/supervisor/conf.d/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# oneapm
pip install -i http://pypi.oneapm.com/simple  --trusted-host pypi.oneapm.com --upgrade blueware



RUN echo "daemon off;" >> /etc/nginx/nginx.conf


ADD . /goge

EXPOSE 80
CMD ["supervisord", "-n"]


