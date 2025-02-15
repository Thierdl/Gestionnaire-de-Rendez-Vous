FROM python:3.12

ENV PYTHONBUFFERED 1

ENV PYTHONDONTWRITECODE 1

RUN mkdir /app 

WORKDIR /app

COPY . /app/

RUN apt-get update && apt-get install -y \
    graphviz \
    libgraphviz-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /env

RUN mkdir -p /mnt/data

COPY project/ /app/project/

ENV PATH="/env/bin/:$PATH"

COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh
RUN python3 -m pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install -r requirements.txt 
