FROM python:3-alpine

WORKDIR /usr/src/app

ENV DATA_SOURCE_URL="to be added"
ENV DATABASE_URL="to be added"

COPY Pipfile .
COPY Pipfile.lock .

RUN pip3 install pipenv
RUN pipenv sync

COPY src ./src
COPY sql ./sql

CMD [ "pipenv", "run", "python", "./src/etl.py" ]