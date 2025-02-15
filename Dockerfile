FROM python:3

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITECODE 1

RUN mkdir /app 

WORKDIR /app

COPY . /app/

RUN python3 -m ven /env

ENV PATH="/env/bin/:$PATH"


RUN python3 -m pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install -r requirements.txt 
