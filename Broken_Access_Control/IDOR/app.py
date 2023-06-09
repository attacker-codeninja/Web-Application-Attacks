from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to the database
db = mysql.connector.connect(
    host='db',
    user='myuser',
    password='mypassword',
    database='mydatabase'
)
# Create a table
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255)
    )
''')

# Commit the changes and close the connection
db.commit()
db.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        #insert the user into the database

        cursor = db.cursor()
        query = "INSERT INTO users (name,email,password) VALUES (%s, %s, %s)"
        values = (name,email,password)
        cursor.execute(query, values)
        db.commit()

        return "Registration succesful"

    return render_template('register.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)