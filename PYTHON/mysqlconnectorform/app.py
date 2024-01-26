from flask import Flask, render_template, request, redirect, flash 
import mysql.connector

app = Flask(__name__)
app.secret_key = 'teddylikeabear'

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
        email VARCHAR(255),
        password VARCHAR(255),
        phone VARCHAR(20),
        birthdate DATE
    )
''')
conn.commit()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    surname = request.form['surname']
    email = request.form['email']
    occupation=request.form['occupation']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    phone = request.form['phone']
    birthdate = request.form['birthdate']

    # Server-side validation
    if password != confirm_password:
        flash('Passwords do not match!', 'error')
        return redirect('/')

    # Insert data into the database
    cursor.execute('INSERT INTO users (name,surname, email, password, phone, birthdate) VALUES (%s, %s, %s, %s, %s)',
                   (name,surname, email, password, phone, birthdate))
    conn.commit()

    flash('Form submitted successfully!', 'success')
    return redirect('/')

@app.route('/users')
def users():
    # Fetch all users from the database
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
