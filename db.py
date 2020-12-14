import psycopg2
from datetime import datetime
from psycopg2.sql import SQL, Identifier
from pgcopy import CopyManager

import config


def connect():
    """
    description
    """
    conn = psycopg2.connect(dbname=config.DB_NAME,
                            user=config.USERNAME,
                            password=config.PASSWORD,
                            host=config.HOSTNAME)
    return conn


def add_person(person):
    """
    description

    Keyword arguments:
    param -- description
    """
    


def add_information():
    """
    description

    Keyword arguments:
    param -- description
    """


def add_relationship():
    """
    description

    Keyword arguments:
    param -- description
    """


def add_intersection():
    """
    description

    Keyword arguments:
    param -- description
    """


def add_content():
    """
    description

    Keyword arguments:
    param -- description
    """


def add_entity():
    """
    description

    Keyword arguments:
    param -- description
    """


def update_():
    """
    description

    Keyword arguments:
    param -- description
    """


def get_():
    """
    description

    Keyword arguments:
    param -- description
    """

connect()