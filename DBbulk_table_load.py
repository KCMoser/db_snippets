import csv
import sqlite3
import logging
#import sys

# Set up timestamp and logfile name
logging.basicConfig(filename='results.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

db_filename = 'test.db'     #enter db filename
data_filename = 'Text.csv'  #enter .csv filename   sys.argv[1] is for keyboard input of filename.

SQL = """
INSERT INTO table1 (first_name, last_name, Client, email, phone)
VALUES (:first_name, :last_name, :Client, :email, :phone)
"""

with open(data_filename, 'rt') as csv_file:
    print (csv_file.read()) #print to check file open ok
    csv_reader = csv.DictReader(csv_file)
    
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.executemany(SQL, csv_reader)
    
#save changes
conn.commit()
logging.info('changes saved')
#close db
conn.close()
logging.info('connection closed')
