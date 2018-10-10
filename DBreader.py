import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

cursor = conn.execute("SELECT first_name, last_name, Client, email, phone from TABLE1")
for row in cursor:
   print ("first_name = ", row[0])
   print ("last_name = ", row[1])
   print ("Client = ", row[2])
   print ("email = ", row[3], "\n")

print ("Operation done successfully")
conn.close()
