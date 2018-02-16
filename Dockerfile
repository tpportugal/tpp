 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip3 install -r requirements.txt
 RUN apt-get update && apt-get install -y graphviz
 ADD . /code/
