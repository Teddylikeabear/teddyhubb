from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Replace these with your MySQL database credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'teddylikeabear',
    'database': 'teddyhubb',
}

# Create a connection to the MySQL database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Create a table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255)
    )
''')
conn.commit()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    # Insert data into the database
    cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
    conn.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
