FROM python:3.9-bookworm

RUN apt update && apt upgrade -y

RUN python3.9 -m ensurepip
RUN python3.9 -m pip install --upgrade pip

ENV POETRY_HOME="/etc/poetry"
ENV PATH="${PATH}:${POETRY_HOME}/bin"
ENV POETRY_VIRTUALENVS_IN_PROJECT=1
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3.9 -
COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install -v --no-root

WORKDIR /app
COPY src /app/src
COPY static /app/static

ENTRYPOINT ["poetry", "run", "python", "src/main/home_periscope.py"]