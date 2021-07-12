
FROM python:3.10-rc-buster

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.lock

