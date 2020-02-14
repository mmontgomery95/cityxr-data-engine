FROM python:3.8 as base

FROM base as builder

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY src /app/src
COPY docker-entry.sh /app/docker-entry.sh
WORKDIR /app
CMD ["./docker-entry.sh"]