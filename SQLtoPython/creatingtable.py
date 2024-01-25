import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "teddyhubb",
	password = "Teddylikeabear2703@",
	database = "teddyhubb"
)

cursor = mydb.cursor()

# Creating a table called 'gfg' in the 
# 'geeksforgeeks' database
cursor.execute("CREATE TABLE gfg (name VARCHAR(255), user_name VARCHAR(255))")
