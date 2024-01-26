# Python program to connect
# to mysql database


import mysql.connector


# Connecting from the server
conn = mysql.connector.connect(user = 'username',
							host = 'localhost',
							database = 'teddyhubb')

print(conn)

# Disconnecting from the server
conn.close()
