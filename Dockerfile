FROM python:3

ADD . /code
WORKDIR /code

RUN pip3 install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
