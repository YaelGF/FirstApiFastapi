FROM ubuntu:20.04
LABEL description = "Tarea 2.1"
RUN apt update
RUN apt upgrade -y

RUN apt-get install -y python3
RUN apt-get install -y sqlite3
RUN apt install -y python3-pip

COPY  requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app

RUN pip install -r requirements.txt

COPY . /opt/app
