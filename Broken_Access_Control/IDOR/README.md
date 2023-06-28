
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

![image](https://github.com/xsudoxx/Web-Application-Attacks/assets/127046919/64924adc-80c4-4709-ab0f-e37e15eaae56)


````
Go into [VSCode]
Open up [Terminal]
git clone https://github.com/xsudoxx/Web-Application-Attacks.git
cd Web-Application-Attacks
cd Cross-Site-Scripting
cd xss
````

### Clear the DB
````
docker volume rm xss_db-data
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
The code you provided is vulnerable to Cross-Site Scripting (XSS) attacks because it directly injects user input into the HTML without proper sanitization or validation.

Specifically, the vulnerable line is:

resultsDiv.innerHTML = "<p>Showing results for: " + query + "</p>";

In this line, the query variable is concatenated directly into the HTML string without any sanitization or encoding. This means that if the user input contains HTML or JavaScript code, it will be rendered and executed as-is, allowing potential malicious code to be injected and executed within the page.

To prevent XSS attacks, it's important to properly sanitize and encode user input before inserting it into the HTML. One way to do this is by using appropriate escaping functions or libraries provided by the framework you're using. In the case of Flask, you can use the |safe filter in Jinja2 templates to mark a variable as safe and prevent auto-escaping.
````
## Updated code
````
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/css/bootstrap.min.css">
  <title>Search Page</title>
  <style>
    .container {
      margin-top: 40px;
    }
  </style>
</head>
<body>
  <!-- Navigation Bar -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
      <a class="navbar-brand" href="#">My Website</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" href="/">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/login">Login</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/register">Register</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/blog">Blog</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/contact">Contact</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/search">Search</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  
  <div class="container">
    <h1>Welcome to our directory Page</h1>

    <div class="row">
      <div class="col-md-6">
        <h2>Search</h2>
        <form method="POST" action="/search">
          <div class="input-group mb-3">
            <input type="text" class="form-control" id="search-input" name="query">
            <button class="btn btn-primary" type="submit">Search</button>
          </div>
        </form>
      </div>
    </div>

    <h2>Search Results</h2>
    <div id="search-results">
      {% if results %}
        {% for result in results %}
          <div class="result-item">
            <h3>{{ result.name }}</h3>
            <p>{{ result.email }}</p>
            <p>{{ result.message | safe }}</p>
          </div>
        {% endfor %}
      {% else %}
        <p>No results found for: {{ query }}</p>
      {% endif %}
    </div>
  </div>

  <script>
    function search() {
      var query = document.getElementById("search-input").value;
      var resultsDiv = document.getElementById("search-results");

      // Properly sanitize and encode user input
      var encodedQuery = document.createElement('div');
      encodedQuery.textContent = query;
      var sanitizedQuery = encodedQuery.innerHTML;

      resultsDiv.innerHTML = "<p>Showing results for: " + sanitizedQuery + "</p>";
    }
  </script>
</body>
</html>
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
