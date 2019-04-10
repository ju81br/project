""" Database utils """

import sqlite3

DB_PATH = 'database.db'
DB_DEFAULT_ERR = sqlite3.Error
DB_INTEGRITY_ERR = sqlite3.IntegrityError


def connect():
    """ return a connection obj (docstring) """
    return sqlite3.connect(DB_PATH)


def dictfetchall(cursor):
    """ returns all rows from a cursor as a dict (docstring) """
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


INSERTY_CITY = """INSERT INTO CITY(id, name, state, country) VALUES(?, ?, ?, ?)"""
INSERTY_RAIN = """INSERT INTO RAIN(date, probability, precipitation, id_city) VALUES(?, ?, ?, ?)"""
INSERT_TEMPERATURE = """INSERT INTO TEMPERATURE (date, min, max, id_city) VALUES (?, ?, ?, ?)"""

QUERY_MAX_TEMP = """
    SELECT c.name city, MAX(t.max) max_temp
      FROM CITY c
      INNER JOIN TEMPERATURE t
      ON c.id = t.id_city
     WHERE t.date BETWEEN DATETIME(?) AND DATETIME(?)
"""

QUERY_AVG_PRECIPITATION = """
    SELECT c.name city, avg(r.precipitation) average
      FROM CITY c 
      INNER JOIN RAIN r
      ON c.id = r.id_city
     GROUP BY c.name;
"""
