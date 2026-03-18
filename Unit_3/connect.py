import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

a=mydb.cursor()

sql = "INSERT INTO student (name, address) VALUES (%s, %s)"
val = [
    ('aa','ratan par'),
    ('bb','ravapar'),
    ('cc','rampar')
    ]

a.executemany(sql, val)

mydb.commit()

print(a.rowcount, "record inserted.")
