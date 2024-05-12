import mysql.connector
mydb = mysql.connector.connect (
    host="localhost",
    user="root",
    passwd = "admin"
)

my_cursor = mydb.cursor( ) #An automated engine
#my_cursor.execute("CREATE DATABASE our_users") #Create Database
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
