# syntax=docker/dockerfile:1.4
FROM python:3.10-slim AS builder

WORKDIR ./app

COPY requirements.txt /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        fonts-liberation && \
    pip install -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

COPY . /

CMD ["python3", "main.py"]

FROM builder as dev-envs

RUN apt-get update

# Установка Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /