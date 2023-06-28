
# insecure direct object references
## Summary
````
https://portswigger.net/web-security/access-control/idor
````
````
Insecure direct object references (IDOR) are a type of access control vulnerability that arises when an application uses user-supplied input to access objects directly. The term IDOR was popularized by its appearance in the OWASP 2007 Top Ten. However, it is just one example of many access control implementation mistakes that can lead to access controls being circumvented. IDOR vulnerabilities are most commonly associated with horizontal privilege escalation, but they can also arise in relation to vertical privilege escalation.
````

## chatgpt summary
````
Cross-Site Scripting (XSS) is a type of web security vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users. It occurs when a web application does not properly validate or sanitize user-generated input before displaying it on a page.
````
## Explaining this to a 5th grader
````
You know how when you visit websites, you can type in things like your name or a message? Well, sometimes bad people try to trick the website and make it show things it shouldn't. They do this by putting special codes or scripts in those input fields that the website doesn't check properly.

When the website shows the things you typed or submitted, it doesn't realize that there might be dangerous scripts hidden in there. So, when other people visit the website and see those things, their computers try to run those scripts without even knowing it. That's when the bad people can do bad things!

For example, they could make a script that steals people's passwords or personal information, or they could even make the website look different and confuse people. It's like a sneaky way of making the website do things it's not supposed to.

To stay safe from XSS, it's important for websites to be very careful about what people can type or submit. They need to check everything properly and make sure it doesn't have any hidden codes or scripts. That way, everyone can use websites without worrying about their information or computer being at risk.
````
## Setup
### Option #1
````
Open Docker and have it running
````

![image](https://github.com/xsudoxx/Web-Application-Attacks/assets/127046919/e9ca8dd6-42f5-48d4-9758-859c84e2a2ce)

````
Go into [VSCode]
Open up [Terminal]
git clone https://github.com/xsudoxx/Web-Application-Attacks.git
cd Web-Application-Attacks
cd Broken_Access_Control
cd IDOR
````

### Clear the DB
````
docker volume rm idor_db-data
````
### Running the vulnerable application
````
docker-compose up
````
### Shutting down the vulnerable application
````
docker-compose down
````
### Option #2
````
Open [Docker Desktop]
Open [VSCODE]
(If you already have Docker Extension added please continue, if not please install it)
Find [docker-compose.yml] & [right-click on the file] & [click][Compose Up]
Hit [Enter]
ctrl + c
docker-compose down
docker-compose up
````

# Code Review
````
 It retrieves user information based on the user_id parameter without any additional authorization or access control checks.

To address the IDOR vulnerability, you need to implement proper authorization and access control mechanisms. Here's an updated version of the code that includes authorization checks:

In this updated code, it first checks if a user is logged in and compares the logged-in user's user_id with the requested user_id. Only if they match, it proceeds to retrieve and display the user's information. Otherwise, it displays an error message indicating unauthorized access.

By implementing these authorization checks, you can mitigate the IDOR vulnerability and ensure that users can only access their own information.
````
## Updated code
````
@app.route('/user/<int:user_id>')
def user_home(user_id):
    if 'user_id' in session:
        logged_in_user_id = session['user_id']
        if logged_in_user_id == user_id:
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
        else:
            flash("Unauthorized access.")
    else:
        flash("Please log in to access this page.")

    return redirect(url_for('login'))

````

# Cyber Security Skills Learned
## Authentication
````
Authentication is the process of verifying the identity of a user or entity to ensure that they are who they claim to be. In the context of computer systems and online services, authentication is crucial for controlling access to resources and protecting sensitive information.
````
### Example 
````
User provides credentials: The user submits their identification information, such as a username or email, and a secret password.
````
## IDOR
````
IDOR stands for Insecure Direct Object Reference. It is a security vulnerability that occurs when an application allows direct access to internal implementation objects or resources without proper authorization checks. In other words, an IDOR vulnerability enables an attacker to access or manipulate sensitive data by modifying a parameter or identifier that directly refers to an internal object or resource.
````
### Example
````
Let's say you have an application that displays user information based on a user ID. The application uses a URL like https://example.com/user?user_id=123 to fetch and display the user's data. In this case, the user_id parameter is directly used to retrieve the user's information from the backend database.

If the application fails to properly validate or authorize the user's access to the requested user ID, an attacker could potentially modify the user_id parameter in the URL to access another user's information. For example, the attacker could change the URL to https://example.com/user?user_id=456 to view the data of a different user without proper authorization.
````
## Access Control
````
The main goal of access control is to protect sensitive information, maintain data confidentiality, integrity, and availability, and prevent unauthorized access or misuse of resources. It helps organizations enforce security policies, comply with regulations, and safeguard their systems and data from both internal and external threats.
````
### Examples
````
Role-Based Access Control (RBAC): Access is granted based on predefined roles assigned to subjects, and permissions are associated with these roles.

Attribute-Based Access Control (ABAC): Access is granted based on evaluating attributes associated with subjects, objects, and environmental conditions.

Mandatory Access Control (MAC): Access decisions are enforced based on security labels or classifications assigned to subjects and objects.

Discretionary Access Control (DAC): Access decisions are determined by the owner of the resource, who grants or revokes permissions.

Rule-Based Access Control: Access decisions are made based on a set of predefined rules or policies.
````
