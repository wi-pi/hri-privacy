import psycopg2
from psycopg2.sql import SQL, Identifier
from datetime import datetime

from data import config


def format_cols(cols, insert=False):
    """
    Formats the columns for selection or insertion.

    Keyword arguments:
    cols -- The list of column names.
    insert -- True uses parenthesis. False does not.
    """
    if insert:
        columns = '('
        args = '('
    else:
        columns = ''
        args = ''
    for i, name in enumerate(cols):
        columns += name
        args += '%s'
        if i < len(cols) - 1:
            columns += ', '
            args += ', '
    if insert:
        columns += ')'
        args += ')'
    return columns, args


def format_where(cols):
    """
    Formats the conditional block for selection or updating.

    Keyword arguments:
    cols -- The list of column names used in the where clause. Does not include data.
    """
    where = ''
    for i, name in enumerate(cols):
        where += '{} IN %s'.format(name)
        if i < len(cols) - 1:
            where += ' AND '
    return where


def format_data(data):
    """
    Formats the data into a tuple for insertion, selection, and updating.

    Keyword arguments:
    data -- The list of data points.
    """
    if data is None:
        return None
    new_data = []
    for i in data:
        new_data.append(tuple(i))
    return new_data


class Database:
    """
    The database class responsible for opening connections, executing, and fetching.
    """
    def __init__(self):
        self.conn = psycopg2.connect(dbname=config.DB_NAME,
                                     user=config.USERNAME,
                                     password=config.PASSWORD,
                                     host=config.HOSTNAME)

    def do(self, sql=None, data=None, file=None, verbose=False):
        """
        Executes an SQL statement and returns the fetched data.

        Keyword arguments:
        sql -- The SQL string to execute.
        data -- The data to pass in for insertion/selection/updating.
        file -- The SQL file to execute. This overwrites the sql and data parameters.
        verbose -- Whether or not to print the SQL statments and results with each function call.
        """
        cur = self.conn.cursor()
        if verbose:
            print(cur.mogrify(sql, data))
        if file is not None:
            cur.execute(open(file, 'r').read())
        else:
            if data is not None:
                cur.execute(sql, data)
            else:
                cur.execute(sql)
        self.conn.commit()
        try:
            temp = cur.fetchall()
            if len(temp) == 0:
                out = None
            else:
                out = []
                if len(temp[0]) == 1:
                    for i in temp:
                        out.append(i[0])
                else:
                    out = temp
        except psycopg2.ProgrammingError:
            out = None
        cur.close()
        if verbose:
            print(out)
        return out

    def insert(self, table, cols, data):
        """
        Constructs an insertion SQL string.

        Keyword arguments:
        table -- The name of the table to insert into.
        cols -- The column names of data to insert.
        data -- The actual data to insert into the database.
        """
        columns, args = format_cols(cols, insert=True)
        sql = 'INSERT INTO {} {} VALUES {} ON CONFLICT DO NOTHING'.format(table, columns, args)
        self.do(sql, data)

    def select(self, table, cols, conds=None, data=None):
        """
        Constructs a selection SQL string.

        Keyword arguments:
        table -- The name of the table to select from.
        cols -- The column names of data to select.
        conds -- The condition column names used in the where clause.
        data -- The conditional data used in the where clause.
        """
        columns, _ = format_cols(cols)
        if conds is not None:
            where = format_where(conds)
            sql = 'SELECT {} FROM {} WHERE {}'.format(columns, table, where)
        else:
            sql = 'SELECT {} FROM {}'.format(columns, table)
        return self.do(sql, format_data(data))

    def update(self, table, cols, conds, data):
        """
        Constructs an update SQL string.

        Keyword arguments:
        table -- The name of the table to update.
        cols -- The column names of data to update.
        conds -- The condition column names used in the where clause.
        data -- The conditional data used in the where clause.
        """
        columns, args = format_cols(cols)
        where = format_where(conds)
        sql = 'UPDATE {} SET {} = {} WHERE {}'.format(table, columns, args, where)
        self.do(sql, format_data(data))

    def delete_all(self):
        self.do(sql='DROP TABLE IF EXISTS content CASCADE;')
        self.do(sql='DROP TABLE IF EXISTS entities CASCADE;')
        self.do(sql='DROP TABLE IF EXISTS information CASCADE;')
        self.do(sql='DROP TABLE IF EXISTS person CASCADE;')
        self.do(sql='DROP TABLE IF EXISTS topic CASCADE;')
        self.do(sql='DROP TABLE IF EXISTS person_content CASCADE;')
        self.do(sql='DROP TABLE IF EXISTS person_information CASCADE;')
        self.do(sql='DROP TABLE IF EXISTS person_trust CASCADE;')
        self.do(sql='DROP TABLE IF EXISTS person_topic CASCADE;')
        self.do(sql='DROP TABLE IF EXISTS information_topic CASCADE;')

    def create_all(self):
        self.do(file='data/create_tables.sql')