FROM ubuntu:latest

RUN apt-fet update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

CMD ["uwsgi", "--ini", "wsgi.ini"]