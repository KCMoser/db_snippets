import sqlite3

#connect to db
conn = sqlite3.connect('test.db')

#create cursor object to execute sql statements
crsr = conn.cursor()

#create table with field info
crsr.execute('''CREATE TABLE table1(
    first_name text,
    last_name text,
    Client text,
    email text,
    phone text)''')

#save changes
conn.commit()

#close db
conn.close()
