FROM python:3.12


ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1


RUN mkdir -p /app /mnt/data
WORKDIR /app


RUN apt-get update && apt-get install -y \
    graphviz \
    libgraphviz-dev \
    && rm -rf /var/lib/apt/lists/*


COPY . /app/
COPY project/ /app/project/


RUN python3 -m venv /env
ENV PATH="/env/bin:$PATH"


RUN python3 -m pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

RUN python3 project/manage.py collectstatic --noinput

ENV PYTHONPATH="/app/project"

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh


EXPOSE 10000


CMD ["/app/entrypoint.sh"]