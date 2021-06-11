# syntax=docker/dockerfile:1

FROM python:3.9.5-slim-buster

WORKDIR /home/leraport

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip3 install --upgrade pip
RUN venv/bin/pip3 install -r requirements.txt
RUN venv/bin/pip3 install gunicorn psycopg2-binary

COPY app app
COPY migrations migrations
COPY leraport.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP leraport.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]

