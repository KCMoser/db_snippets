import csv
import sqlite3
import logging

# Set up timestamp and logfile name
logging.basicConfig(filename='results.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

#pull csv file in as a dictionary
csv_reader = csv.DictReader(open('Text.csv'))
for row in csv_reader:
    print (row)

#connect to database
conn = sqlite3.connect('test.db')
#create cursor object to execute commands
cursor = conn.cursor()
cursor.executemany('''INSERT INTO table1 (first_name, last_name, Client, email, phone) VALUES (:first_name, :last_name, :Client, :email, :phone)''' , csv_reader)
    
#save changes
conn.commit()
#logging.info('changes saved')
print('changes saved')

#close db
conn.close()
#logging.info('connection closed')
print('database closed')
