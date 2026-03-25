'''import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb) '''



'''import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")'''



'''import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x) '''



'''import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)'''



'''import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
'''



'''import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)'''



'''import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")'''



'''import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")'''



'''import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")'''



'''import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")'''



'''import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)'''



import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

a=mydb.cursor()

'''sql = "INSERT INTO student (name, address) VALUES (%s, %s)"
val = [
    ('aa','rajkot'),
    ('bb','ratan par')
    ]

a.executemany(sql, val)

mydb.commit()

print(a.rowcount, "record inserted.")'''




'''a.execute("SELECT * FROM student")

show = a.fetchall()

for x in show:
    print(x)'''



'''a.execute("SELECT name, address FROM student")

show = a.fetchall()

for x in show:
  print(x)'''



'''a.execute("SELECT * FROM student")

show = a.fetchone()

print(show)'''



'''sql = "SELECT * FROM student WHERE address ='ratan par'"

a.execute(sql)

show = a.fetchall()

for x in show:
    print(x)'''



'''sql = "SELECT * FROM student WHERE name ='aa'"

a.execute(sql)

show = a.fetchall()

for x in show:
    print(x)'''



'''sql = "DELETE FROM student WHERE address = %s"
value = (input("Enter The Address : "),)

a.execute(sql, value)
mydb.commit()

if a.rowcount == 0:
    print("record(s) not found")
else:
    print(a.rowcount, "record(s) Deleted")'''



sql = "UPDATE student SET address = %s WHERE address = %s"
old = input("Enter The Old Address : ")
new = input("Enter The New Address : ")

values = (new, old)

a.execute(sql, values)
mydb.commit()

if a.rowcount == 0:
    print("record(s) not found")
else:
    print(a.rowcount, "record(s) UPDATED")



'''a.execute("SELECT * FROM student LIMIT 1")

show = a.fetchall()

for x in show:
    print(x)'''
