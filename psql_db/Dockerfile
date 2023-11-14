# syntax=docker/dockerfile:1

FROM python:3.10.12-slim-buster

LABEL maintainer "Timothy Ko <tk2@illinois.edu>"
RUN apt-get update
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_ENV="docker"
EXPOSE 5000
