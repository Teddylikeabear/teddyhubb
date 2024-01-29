import MySQLdb

# Replace these values with your actual MySQL server details
mysql_host = "localhost"
mysql_user = "teddy"
mysql_password = "Teddylikeabear2703@"
mysql_database = "teddyhubb"

# Test the connection
try:
    connection = MySQLdb.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_database
    )
    print("MySQL Connection Successful!")
except Exception as e:
    print(f"Error: {e}")
finally:
    if connection:
        connection.close()
