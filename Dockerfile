FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y python3-pip
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
ENV FLASK_APP app.py
ENV FLASK_ENV development
EXPOSE 5000
CMD [ "flask", "run"]