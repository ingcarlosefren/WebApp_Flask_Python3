FROM python:3.8-slim-buster

WORKDIR /flask_webapp_cefa

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python3","./app/main.py"]