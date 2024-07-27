FROM python:3.10-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONHONUNBUFFERED 1

WORKDIR /track-gym-shop

RUN apt update -y && \
    apt install -y python3-dev \
    gcc \
    musl-dev

ADD pyproject.toml /track-gym-shop

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY . /track-gym-shop