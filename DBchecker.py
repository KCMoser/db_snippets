import csv
import sqlite3

#connect to db
con = sqlite3.connect('test.db')
#create cursor object to execute sql statements
crsr = con.cursor()
#enter search criteria if any here..
sql = 'SELECT * FROM table1'
#execute and print table contents
crsr.execute(sql)
print (crsr.fetchall())
#close db
con.close()
