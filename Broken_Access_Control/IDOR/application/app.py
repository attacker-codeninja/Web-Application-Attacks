from flask import Flask, render_template, request, redirect, url_for, session, flash
import logging
import mysql.connector

# Set up logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.secret_key = 'password-test'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']

            # Connect to the database and retrieve the user
            db = mysql.connector.connect(
                host='db',
                user='myuser',
                password='mypassword',
                database='mydatabase'
            )
            cursor = db.cursor()
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            values = (email, password)
            cursor.execute(query, values)
            user = cursor.fetchone()

            # Close the connection
            db.close()

            if user:
                # Store the user's information in the session
                session['user_id'] = user[0]
                session['name'] = user[1]
                session['email'] = user[2]
                session['password'] = user[3]

                if user[4] == 'admin':
                    # Store the admin status in the session
                    session['is_admin'] = True

                    # Redirect the admin user to the admin.html page
                    return redirect(url_for('admin'))

                # Redirect to the user's home page
                return redirect(url_for('user_home', user_id=user[0]))

            else:
                flash("Invalid email or password. Please try again.")
                return redirect(url_for('login'))

        except Exception as e:
            # Log the error
            logging.error(f"Error during login: {str(e)}")
            flash("An error occurred during login. Please try again later.")

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

            # Insert the user into the database with the 'user' role
            query = "INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)"
            values = (name, email, password, 'user')
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



@app.route('/user/<int:user_id>')
def user_home(user_id):
    # Retrieve user information from the database based on the user_id
    db = mysql.connector.connect(
        host='db',
        user='myuser',
        password='mypassword',
        database='mydatabase'
    )
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE id = %s"
    values = (user_id,)
    cursor.execute(query, values)
    user = cursor.fetchone()
    db.close()

    if user:
        name = user['name']
        email = user['email']
        password = user['password']

        return render_template('home.html', name=name, email=email, user_id=user_id, password=password)
    else:
        flash("User not found.")

    return redirect(url_for('login'))



@app.route('/admin')
def admin():
    # Check if the user is logged in as an admin
    if session.get('is_admin'):
        # Get the admin's email and name from the session or database
        email = session['email']  # Update this with the key used to store the email in the session
        name = session['name']  # Update this with the key used to store the name in the session

        # Render the admin.html template and pass the email and name as template variables
        return render_template('admin.html', email=email, name=name,is_admin=True)
    else:
        # Redirect non-admin users to a different page or display an error message
        return redirect(url_for('login'))



@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
