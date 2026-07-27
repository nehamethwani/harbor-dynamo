FROM python:3.13-slim-bookworm@sha256:REPLACE_WITH_DIGEST_YOU_PULL_YOURSELF

WORKDIR /app

RUN pip install --no-cache-dir \
    pytest==8.3.4 \
    pytest-json-ctrf==0.3.3

COPY sales.csv /app/sales.csv
