import sqlite3

#connect to db
con = sqlite3.connect('test.db')
#create cursor object to execute sql statements
crsr = con.cursor()
#execute a statement
crsr.execute('''INSERT INTO table1 (first_name, last_name, Client, email, phone) VALUES (?, ?, ?, ?, ?)''', ('myfirstname', 'mylastname', 'Tecniplast', 'newemail', 'newphone'))

#save change
con.commit()

#close db
con.close()
