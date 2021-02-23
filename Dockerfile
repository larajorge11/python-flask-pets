FROM python:3.9.2

MAINTAINER "Jorge Lara"

RUN mkdir -p /flask-pets-app

WORKDIR /flask-pets-app

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . /flask-pets-app

EXPOSE 5000

ENV FLASK_APP="src/main.py"

CMD ["flask", "run", "-h", "0.0.0.0"]
