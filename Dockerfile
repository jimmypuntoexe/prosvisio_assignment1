#use a Python image as our launching point
FROM python:3.7

WORKDIR /ticketapp

COPY . /

RUN apt-get update

RUN pip install mysql-connector-python

RUN pip install pylint
#CMD ["python", "test.py"]

