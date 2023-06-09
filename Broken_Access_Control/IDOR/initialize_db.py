import mysql.connector

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
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255)
    )
''')

# Close the connection
db.close()
