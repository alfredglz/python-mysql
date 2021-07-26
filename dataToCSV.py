# This is a practices to get data from a database and convert it to a CSV file using csv module
from connection import db
import csv
import sys

# Obtain data from a database
cursor = db.cursor()
sql = "SELECT purchase, date, time, users.username FROM purchases INNER JOIN users ON purchases.user_id = users.user_id"
headers = ['purchase', 'date', 'time', 'username']
cursor.execute(sql)
result = cursor.fetchall()

# Create a csv file
f = open('data.csv', 'wt')

# Insert data to the file
try:
    filewriter = csv.writer(f)
    # filewriter.writerow(headers)    
    for n in result:
        filewriter.writerow([n[0], n[1], n[2], n[3]])
    # filewriter.writerows(result)
finally:
    f.close()        
