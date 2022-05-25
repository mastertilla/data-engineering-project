FROM python:3.9

RUN apt-get install wget

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.0

# System deps
RUN pip install poetry==${POETRY_VERSION}
ENV PATH $HOME/.poetry/bin:$PATH
WORKDIR /app
COPY poetry.lock pyproject.toml ./

# Project initialization
RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi

# Creating folders, and files for a project
COPY data_analysis.py /app

ENTRYPOINT [ "python", "data_analysis.py" ]