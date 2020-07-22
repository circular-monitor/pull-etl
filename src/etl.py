import os
import urllib.request
import json
from sqlalchemy import create_engine


def get_data(url):
    response = urllib.request.urlopen(url)
    parsed = json.loads(response.read())
    return parsed


def clean(data):
    return data


def insert(database_url, clean_data):
    database_engine = create_engine(database_url)

    with database_engine.begin() as connection, open('sql/schema.sql') as schema_file:
        schema = ''.join(schema_file.readlines())
        connection.execute(schema)
        # TODO: Insert data


if __name__ == '__main__':
    data_source_url = os.getenv('DATA_SOURCE_URL')
    database_url = os.getenv('DATABASE_URL')

    data = get_data(data_source_url)
    clean_data = clean(data)
    insert(database_url, clean_data)
