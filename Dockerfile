#use a Python image as our launching point
FROM python:2.7

WORKDIR /ticketapp

COPY . /

RUN apt-get update

RUN pip install mysql-connector-python

#CMD ["python", "test.py"]

