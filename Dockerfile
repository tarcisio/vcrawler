FROM python:3.6-onbuild

ENTRYPOINT ["scrapy"]
CMD [ "-h" ]
