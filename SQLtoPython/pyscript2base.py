import sqlite3

# Connect to the SQLite database (or replace with your database connection details)
conn = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table (replace with your own table creation SQL)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Insert data into the table
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('teddy', 'nyatshiisana@gmail.com'))

# Commit the changes and close the connection
conn.commit()

# Fetch and print the data from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Users in the database:")
for row in rows:
    print(row)

# Close the connection
conn.close()
