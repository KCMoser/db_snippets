import sqlite3

#connect to db
con = sqlite3.connect('test.db')
#create cursor object to execute sql statements
crsr = con.cursor()
#execute a statement
crsr.execute('''SELECT first_name, last_name, Client, email, phone FROM table1''')
#extract all info
alldata = crsr.fetchall()
for row in alldata:
    print('{0} : {1} : {2} : {3} : {4}'.format(row[0], row[1], row[2], row[3], row[4]))
#close db
con.close()
