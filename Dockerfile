FROM python:3.12

WORKDIR /user_api/

RUN pip install poetry

COPY pyproject.toml poetry.lock README.md __init__.py /user_api/

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . /user_api/

RUN chmod a+x /user_api/script/run.sh
