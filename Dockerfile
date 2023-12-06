FROM python:3.11-slim as base

WORKDIR /app

RUN pip install poetry

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    PYTHONPATH="/app"

COPY pyproject.toml poetry.lock /app/

RUN poetry install $(test "$ENVIRONMENT" = production && echo "--only main") --no-ansi || :

FROM base as final

COPY src /app/src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
