FROM python:3.5.5-slim-jessie
COPY ./app /app

RUN apt-get update; \
    apt-get -y install cron python3-pip; \
    mv /app/feed-cron /etc/cron.d/; \
    chmod 0644 /etc/cron.d/feed-cron; \
    touch /var/log/cron.log; \
    pip3 install feedparser xmljson;


VOLUME ['/app/data/']
WORKDIR /app/data/
CMD cron && tail -f /var/log/cron.log
#CMD ["/usr/local/bin/python3.5", "-m", "http.server", "80"]
