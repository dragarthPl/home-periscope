FROM python:3.11-bookworm

RUN apt update && apt upgrade -y

RUN curl -fsSL https://deb.nodesource.com/setup_21.x | bash - && apt install -y nodejs
RUN corepack enable pnpm

RUN python3.11 -m ensurepip
RUN python3.11 -m pip install --upgrade pip

# Building python
ENV POETRY_HOME="/etc/poetry"
ENV PATH="${PATH}:${POETRY_HOME}/bin"
ENV POETRY_VIRTUALENVS_IN_PROJECT=1
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3.11 -
COPY poetry.lock .
COPY pyproject.toml .
COPY frontend/package.json /app/frontend/

RUN cd /app/frontend && pnpm install
RUN poetry install -v --no-root

WORKDIR /app
COPY frontend/src /app/frontend/src
COPY frontend/public /app/frontend/public
COPY frontend/.env /app/frontend/

RUN cd /app/frontend && pnpm build
COPY src /app/src

ENTRYPOINT ["poetry", "run", "python", "src/main/home_periscope.py"]
