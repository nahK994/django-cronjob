FROM python:3.11

USER root
RUN apt-get -y update
RUN apt-get install -y cron

ENV TZ=Asia/Dhaka

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3 manage.py makemigrations
