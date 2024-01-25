import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "teddyhubb",
	password = "Teddylikeabear2703@"
)

# Creating an instance of 'cursor' class 
# which is used to execute the 'SQL' 
# statements in 'Python'
cursor = mydb.cursor()

# Creating a database with a name
# 'geeksforgeeks' execute() method 
# is used to compile a SQL statement
# below statement is used to create 
# the 'geeksforgeeks' database
cursor.execute("CREATE DATABASE teddyhubb ")
