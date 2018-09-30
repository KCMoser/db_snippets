import sqlite3
from sqlite3 import Error

#create connection object to db, if it doesn't exist, db is created.
def create_db(dbc):
    try:
        conn = sqlite3.connect(dbc)
        print('Database creation complete')
    except Error as e:
        print(e)
    finally:
        #close db
        conn.close()
if __name__ == '__main__':
    #enter database name below
    create_db("test.db")
