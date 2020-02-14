FROM python:3.8-alpine as base
RUN apk add --no-cache bash

FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local
COPY src /app/src
COPY docker-entry.sh /app/docker-entry.sh

WORKDIR /app

CMD ["./docker-entry.sh"]