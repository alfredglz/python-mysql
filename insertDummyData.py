# Generating masive random data using a module called "faker" and insert it to a database
from connection import db
from faker import Faker
import random

fake = Faker()
cursor = db.cursor()

data = list()
fake_data = list()

for _ in range(100):    
    fake_data.append(fake.unique.text())
    fake_data.append(fake.unique.date_this_year())
    fake_data.append(fake.unique.time())
    fake_data.append(random.randrange(1, 12))
    data.append(list(fake_data))
    fake_data.clear()

sql = "INSERT INTO purchases (purchase, date, time, user_id) VALUES (%s, %s, %s, %s)"

cursor.executemany(sql, data)
db.commit()

print(cursor.rowcount, "records inserted")