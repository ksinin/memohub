FROM python:3.10.4-bullseye

ARG ENV

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_NO_INTERACTION=1 \
    POETRY_NO_ANSI=1 \
    POETRY_VIRTUALENVS_CREATE=false

RUN pip install poetry

RUN mkdir /src /internal
WORKDIR  /src

COPY ./bin /internal/
COPY ./src/poetry.lock ./src/pyproject.toml /src/
RUN poetry install $(if [ "$ENV" = 'production' ]; then echo '--no-dev'; fi)

COPY ./src /src/
