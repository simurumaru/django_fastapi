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

#RUN poetry run python src/manage.py collectstatic --noinput
#
#CMD ["poetry", "run", "uvicorn", "server.asgi:app", "--host", "0.0.0.0", "--port", "8000"]

ENTRYPOINT ["make", "start-prod"]