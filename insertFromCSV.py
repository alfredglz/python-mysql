# This is a practice to insert records from a CSV file to a MySQL database

from connection import db
import pandas as pd

cursor = db.cursor()

df = pd.read_csv('test.csv')

y1 = tuple(df['username'])
y2 = tuple(df['email'])
val = list()

for n in range(len(y1)):
    append = list()
    append.append(y1[n])
    append.append(y2[n])
    val.append(tuple(append))

sql = "INSERT INTO users (username, email) VALUES (%s, %s)" # query to insert data in a table

cursor.executemany(sql, val) # query and values
db.commit()
print(cursor.rowcount, "record inserted")
    