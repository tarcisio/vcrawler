FROM python:3

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /app
WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["scrapy"]
CMD [ "-h" ]
