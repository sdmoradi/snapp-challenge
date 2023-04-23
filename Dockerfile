FROM registry.docker.ir/library/python:3.10

WORKDIR /app
COPY requirements.txt requirements.txt
COPY resolv.conf /etc/resolv.conf

RUN pip config --user set global.index-url https://nexus.frox.ir/repository/pypi/simple
RUN pip install -U pip
RUN pip install -r requirements.txt

ARG PORT=5000
EXPOSE ${PORT}
COPY app/. .


ARG FLASK_APP=app.py
CMD flask run --host=0.0.0.0 

