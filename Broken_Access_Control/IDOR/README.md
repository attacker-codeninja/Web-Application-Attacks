
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
## Framework Auto Encoding
````
Flask provides some built-in features and libraries that can help mitigate XSS vulnerabilities:

Template Engine: Flask uses a template engine, such as Jinja, which has built-in automatic escaping. By default, Jinja escapes all content rendered in templates unless explicitly marked as safe using the safe filter. This helps prevent unintentional XSS vulnerabilities by automatically escaping user input.

Manual Escaping: Flask provides a Markup class that allows you to manually mark a string as safe when you are confident that it does not contain any malicious content. However, it is generally recommended to use the safe filter within templates to mark specific variables as safe, instead of relying on manual escaping.
````
### Example 
````
<p>{{ result.message | safe }}</p>
{% autoescape true %}
{% endautoescape %}
````
## XSS
````
XSS attacks can be classified into three main types:

Stored XSS: The injected malicious code is permanently stored on the target server, often within a database. Whenever a user requests the affected page, the stored script is retrieved and executed in the user's browser.

Reflected XSS: The injected script is embedded in a URL or other input fields and is reflected back to the user by the server without proper sanitization. The script is executed in the victim's browser when they click on a malicious link or submit a form.

DOM-based XSS: This type of XSS occurs when the vulnerability is within the client-side JavaScript code, manipulating the Document Object Model (DOM) of a web page. The malicious script modifies the page's structure or behavior, leading to unexpected consequences and potential security risks.

The impact of XSS attacks can be severe, including:

Theft of sensitive user data, such as login credentials, personal information, or cookies.
Session hijacking, where the attacker gains unauthorized access to a user's active session.
Defacement of websites by modifying the content or layout.
Distribution of malware or phishing attacks through infected web pages.
Social engineering attacks to deceive users or gain their trust.
To prevent XSS attacks, web developers should implement proper input validation and output encoding/sanitization techniques. This includes:

Validating and filtering user input to ensure it conforms to the expected format.
Encoding user-generated content before displaying it on web pages to prevent script execution.
Implementing Content Security Policy (CSP) to restrict the types of content that can be loaded on a page.
Using frameworks and libraries that automatically handle input sanitization and output encoding.
Educating developers about secure coding practices and the risks associated with XSS vulnerabilities.
By taking these precautions, web applications can mitigate the risk of XSS attacks and ensure the safety of their users' browsing experience.
````
### Example payloads
````
https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection
````
## Sanatizing Code
````
Sanitizing code, in the context of cybersecurity, refers to the process of cleaning and validating user input to remove or neutralize potentially malicious or harmful elements. It is an essential practice to prevent code injection attacks, specifically cross-site scripting (XSS) attacks.
````
### Examples
#### PHP
````
$input = '<script>alert("XSS Attack");</script>';
$sanitizedInput = htmlspecialchars($input, ENT_QUOTES, 'UTF-8');
echo $sanitizedInput;
````
#### Python (Django framework)
````
{% autoescape on %}
  {{ user_input }}
{% endautoescape %}
````
#### JavaScript
````
var user_input = '<script>alert("XSS Attack");</script>';
var sanitizedInput = DOMPurify.sanitize(user_input);
document.getElementById('output').innerHTML = sanitizedInput;
````
#### Ruby on Rails
````
user_input = '<script>alert("XSS Attack");</script>'
sanitized_input = sanitize(user_input, tags: [])
puts sanitized_input
````
#### Java (Spring framework)
````
import org.springframework.web.util.HtmlUtils;

String userInput = "<script>alert(\"XSS Attack\");</script>";
String sanitizedInput = HtmlUtils.htmlEscape(userInput);
System.out.println(sanitizedInput);
````

