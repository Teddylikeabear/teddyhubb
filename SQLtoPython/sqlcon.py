# Importing module 
import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
	host = "localhost",
	user = "teddyhubb",
	password = "Teddylikeabear2703@"
)

# Printing the connection object 
print(mydb)

