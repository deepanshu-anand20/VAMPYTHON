import mysql.connector
# create database connection to mysql
connection = mysql.connector.connect(host = "localhost", username = "root", password = "Aa9354788705bB", database = "event")
# to check if the connectiojn is established or not.
if connection.is_connected():
    print("Dataase is connected.")
else:
    print("Database is not connected.") 

# to create user table in databse
users = "create table if not exists users(fname text)"
# to pass the cursor handle sql query.   
mycursor = connection.cursor()
# to execute the sql query
mycursor.execute(users)
connection.commit()
# to insert fname in users table
insertName = "insert into users values('{}')".format("deepanshu anand")
mycursor.execute(insertName)
connection.commit()