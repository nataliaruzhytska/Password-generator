 # pull official base image
FROM python:3.7

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . /usr/src/app/

# set work directory
WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
