#python -m pip install mysql-connector-python
import mysql.connector
myDataBase = mysql.connector.connect(
    host = "localhost",
    user ="root",
    database ="testing_database"  
)
mycursor = myDataBase.cursor()#used to make a platform  tp run query language
# mycursor.execute("Create database testing_database")#used to create a database
mycursor.execute("Create table students (name VARCHAR(255), age INTEGER(10))")#used to create a table


print(myDataBase)