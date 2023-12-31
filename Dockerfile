FROM python:3.11.5

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
CMD ["python3","-m","django","run","--host=0.0.0.0"]
