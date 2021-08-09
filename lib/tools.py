# -*- coding: utf-8 -*-
import sys
import yaml
import pandas as pd


def get_db_uri(type, host, port, db, user, password, **kwargs):
    return f'{type}://{user}:{password}@{host}:{port}/{db}'


def get_db_connection_string(host, port, db, user, password, **kwargs):
    return f"host='{host}' dbname='{db}' port={port} user='{user}' password='{password}'"


def read_config(path):
    with open(path, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            sys.exit(exc)
    return config


def configure_pandas(max_rows=None, max_columns=None, max_width=None, max_colwidth=None, logger=None):
    pd.set_option('display.max_rows', max_rows)
    pd.set_option('display.max_columns', max_columns)
    pd.set_option('display.max_colwidth', max_colwidth)
    pd.set_option('display.width', max_width)
    pd.set_option('display.expand_frame_repr', True)
