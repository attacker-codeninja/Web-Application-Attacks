from flask import Flask, render_template, request,redirect,url_for,flash
import mysql.connector
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.secret_key = 'password-test'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']

            # Connect to the database and check if the user is already registered
            db = mysql.connector.connect(
                host='db',
                user='myuser',
                password='mypassword',
                database='mydatabase'
            )
            cursor = db.cursor()
            query = "SELECT * FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            user = cursor.fetchone()

            if user:
                # User already exists, show flash message and redirect to login
                flash("User already registered. Please log in.")
                db.close()
                return redirect(url_for('login'))
            
            # Insert the user into the database
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            values = (name, email, password)
            cursor.execute(query, values)
            db.commit()
            db.close()

            logging.info("Registration successful")
            flash("Registration successful. Please log in.")
            return redirect(url_for('login'))

        except Exception as e:
            # Log the error
            logging.error(f"Error during registration: {str(e)}")
            return "An error occurred during registration. Please try again later."

    return render_template('register.html')



@app.route('/user/<name>')
def user_home(name):
    email = request.args.get('email')
    return render_template('home.html', name=name, email=email)

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
