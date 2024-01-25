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

# Show database
cursor.execute("SHOW DATABASE")

for x in cursor:
  print(x)
