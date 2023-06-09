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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Insert the user into the database
        cursor = db.cursor()
        query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        values = (name, email, password)
        cursor.execute(query, values)
        db.commit()

        return "Registration successful"

    return render_template('register.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
