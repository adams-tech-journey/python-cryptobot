FROM python:3

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
WORKDIR /cryptobot
COPY cryptobot .
RUN pip install -r ./requirements.txt 
ENV PYTHONPATH /cryptobot

CMD [ "python", "main.py" ]


