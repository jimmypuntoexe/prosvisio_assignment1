#use a Python image as our launching point
FROM python:3

WORKDIR /ticketapp





COPY requirements.txt /tmp
WORKDIR /tmp
RUN apt-get update
#RUN pip install mysql-connector-python
RUN pip install -r requirements.txt
RUN pip install pyflakes
#RUN pip install mysql

COPY . /

CMD ["python", "test.py"]
