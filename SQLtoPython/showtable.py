import mysql.connector

mydb = mysql.connector.connect
(
	host = "localhost",
	user = "teddyhubb",
	password = "Teddylikeabear2703@",
	database = "teddyhubb"
)

cursor = mydb.cursor()

# Show existing tables
cursor.execute("SHOW TABLES")

for x in cursor:
 print(x)
