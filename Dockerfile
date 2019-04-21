FROM python:3.7
ENV PYTHONUNBUFFERED=1

ADD . /code/
WORKDIR /code
RUN pip install -r requirements.txt

ENTRYPOINT ["./docker-entrypoint.sh"]