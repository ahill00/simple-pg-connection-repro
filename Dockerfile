FROM python:2.7

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

# RUN python ./setup.py install

EXPOSE 9001

ENV PYTHONPATH /app

COPY uwsgi.ini /config/uwsgi.ini
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

VOLUME ["/config"]

ENTRYPOINT ["docker-entrypoint.sh"]

