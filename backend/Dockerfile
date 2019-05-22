FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

ARG requirements=development.txt

WORKDIR /app

# Application packages
RUN apk add --update --no-cache --virtual .run-deps bash libpq && rm -rf /var/cache/apk/*

COPY requirements/ ./requirements/

RUN apk add --update --no-cache --virtual .build-deps \
        gcc \
        libffi-dev \
        musl-dev \
        linux-headers \
        postgresql-dev \
        git \
    && rm -rf /var/cache/apk/* \
    && pip install --upgrade pip==19.0.2 \
    && pip install --no-cache-dir -r requirements/$requirements \
    && apk del .build-deps

COPY project .
