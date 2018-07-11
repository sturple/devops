FROM python:3.5.5-slim-jessie

COPY server.py /app/
RUN apt-get update; \
    chmod +x /app/server.py ;

EXPOSE 80/tcp

CMD ["/usr/local/bin/python3.5", "/app/server.py"]
