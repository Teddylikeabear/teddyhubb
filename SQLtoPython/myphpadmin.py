import mysql.connector

# Connect to MySQL server (adjust the parameters based on your XAMPP configuration)
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
)


cursor = connection.cursor()


database_name = "teddyhubb"


create_database_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"


cursor.execute(create_database_query)


connection.commit()
cursor.close()
connection.close()

print(f"Database '{database_name}' created successfully.")
