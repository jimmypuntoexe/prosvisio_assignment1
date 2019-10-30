#use a Python image as our launching point
FROM python:3

WORKDIR /ticketapp



RUN apt-get update

RUN pip install mysql-connector-python
RUN apt-get install python3-mysql.connector
COPY requirements.txt /tmp
WORKDIR /tmp

RUN pip install -r requirements.txt
RUN pip install pylint

COPY . /

CMD ["python", "test.py"]
