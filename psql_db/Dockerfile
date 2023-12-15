# syntax=docker/dockerfile:1

FROM python:3.10.12-slim-buster

RUN apt-get update
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install psycopg2-binary
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_ENV="docker"
EXPOSE 8888
