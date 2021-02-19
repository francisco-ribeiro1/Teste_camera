FROM python:3.8

USER root

WORKDIR /usr/src/app

ADD requirements.txt ./requirements.txt
ADD takePicture.py ./takePicture.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#RUN pip install gpiozero
#RUN pip install picamera
#RUN pip install DateTime
#RUN pip install signal
#RUN pip install time

