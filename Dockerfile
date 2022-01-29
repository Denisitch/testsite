FROM python:3.8
MAINTAINER Denis Osyushkin

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y sudo vim && apt-get upgrade -y

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip -r /requirements.txt

RUN mkdir /mysite
WORKDIR /mysite
COPY ./mysite /mysite