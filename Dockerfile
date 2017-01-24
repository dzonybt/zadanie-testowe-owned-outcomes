FROM python:2.7
RUN mkdir /code
ADD requirements.txt /code/requirements.txt
WORKDIR /code/
RUN pip install -r requirements.txt
RUN adduser --disabled-password --gecos '' dzonybt