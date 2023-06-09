from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Perform your login validation here
        # You can check against a database or any other authentication mechanism

        return redirect(url_for('success'))

    return render_template('login.html')

@app.route('/success')
def success():
    return 'Login Successful!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
