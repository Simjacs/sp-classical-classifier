FROM tensorflow/tensorflow:latest-gpu

# install python 3.8
RUN apt-get install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y python3.8

# install requirements
COPY requirements.txt .
RUN /usr/bin/python3.8 -m pip install --upgrade pip
RUN /usr/bin/python3.8 -m pip install --no-cache-dir -r requirements.txt
