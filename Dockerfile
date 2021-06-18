FROM tensorflow/tensorflow:latest-gpu

COPY requirements.txt .

RUN apt-get install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y python3.8

RUN /usr/bin/python3.8 -m pip install --upgrade pip
RUN /usr/bin/python3.8 -m pip install --no-cache-dir -r requirements.txt
