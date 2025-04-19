FROM python:3.12-slim

RUN apt-get update && apt-get install -y libpq-dev gcc gettext make && rm -rf /var/lib/apt/lists/*

ENV WORKDIR=/usr/src/app
ENV PYTHONPATH=$WORKDIR/src

WORKDIR /usr/src/app

RUN pip install poetry

COPY Makefile $WORKDIR/
COPY pyproject.toml poetry.lock $WORKDIR/
RUN poetry update
COPY ./src $WORKDIR/src

ENTRYPOINT ["make", "start-prod"]
