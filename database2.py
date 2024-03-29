import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "python_tc" # STEP 2
)
mycursor = db.cursor()
# mycursor.execute('Create database python_tc') STEP 1 save and run this line
# mycursor.execute('CREATE TABLE persons (PersonID int, LastName VARCHAR(255),)')# STEP 3
# mycursor.execute('INSERT INTO persons (PersonID,LastName) VALUES (1,"Khadka")') # STEP 4
# mycursor.execute('INSERT INTO persons (PersonID,LastName) VALUES (2,"Nirpesh"),(3,"Pragyan")') # STEP 5
# mycursor.execute('CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))')
# db.commit()
# print(db)
# sql = "INSERT INTO customers(name,address) VALUES(%s,%s)"
# val =[
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')

#   ]
# mycursor.executemany(sql,val)
# db.commit()

# mycursor.execute('SELECT * FROM customers')
# result = mycursor.fetchall()
# print(mycursor.rowcount)


mycursor.execute('SELECT * FROM customers WHERE address = "Park Lane 38"')
result = mycursor.fetchall()

# mycursor.execute('DELETE * FROM customers ')
# result = mycursor.fetchall()
# db.commit()
