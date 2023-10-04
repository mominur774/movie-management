FROM python:3.8-slim-buster

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app

COPY ./ /app

WORKDIR /app

RUN chmod +x /app/entrypoint.sh
RUN chmod +x /app/media

CMD ["/app/entrypoint.sh"]