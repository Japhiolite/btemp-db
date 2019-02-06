import sqlite3
import pandas as pd 

def connect(db_file):
    """
    Connect to an existing sqlite database file
    :param db_file: string - path to database file
    :return: connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        return conn, c
    except sqlite3.Error as err:
        print(err)

def close(conn, commit='Yes'):
    """close connection to the database, commit or dont"""
    if commit == 'Yes':
        conn.commit()
    conn.close()

def get_tables(c):
    """get all table names in the database"""
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(c.fetchall())
    return c.fetchall()

def get_columns(c,table):
    """get all columns in a specified table"""
    head = c.execute("select * from " + table)
    names = list(map(lambda x: x[0], nam.description))
    
    print(names)
    return(names)
