# Cross Site Scripting Attacks
## Summary
````
https://portswigger.net/web-security/cross-site-scripting#what-is-cross-site-scripting-xss
````
````
Cross-site scripting (also known as XSS) is a web security vulnerability that allows an attacker to compromise the interactions that users have with a vulnerable application. It allows an attacker to circumvent the same origin policy, which is designed to segregate different websites from each other. Cross-site scripting vulnerabilities normally allow an attacker to masquerade as a victim user, to carry out any actions that the user is able to perform, and to access any of the user's data. If the victim user has privileged access within the application, then the attacker might be able to gain full control over all of the application's functionality and data.
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
````
## Updated code
````
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

    // Create a text node containing the sanitized query
    var textNode = document.createTextNode("Showing results for: " + sanitizedQuery);

    // Clear the existing content of the resultsDiv
    resultsDiv.innerHTML = '';

    // Append the textNode to the resultsDiv
    resultsDiv.appendChild(textNode);
  }
</script>
````
### Explanation
````
In this line, the query variable is concatenated directly into the HTML string without any sanitization or encoding. This means that if the user input contains HTML or JavaScript code, it will be rendered and executed as-is, allowing potential malicious code to be injected and executed within the page.

To prevent XSS attacks, it's important to properly sanitize and encode user input before inserting it into the HTML. One way to do this is by using appropriate escaping functions or libraries provided by the framework you're using. In the case of Flask, you can use the |safe filter in Jinja2 templates to mark a variable as safe and prevent auto-escaping.

In this updated code, the user input is properly sanitized by creating a new div element and setting its textContent to the user input. By retrieving the innerHTML of this div element, any potentially harmful HTML tags or characters are encoded.

Instead of using innerHTML to directly inject the user input into the HTML, a new text node is created using document.createTextNode(). The sanitized query is appended as the text content of this text node, ensuring that it is treated as plain text and not interpreted as HTML or script code.

By following this approach, the user input is properly sanitized and prevents any malicious code from being executed in the context of the webpage.
````

# Cyber Security Skills Learned
## XSS
````
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
### Example
````
XSS attacks can be classified into three main types:

Stored XSS: The injected malicious code is permanently stored on the target server, often within a database. Whenever a user requests the affected page, the stored script is retrieved and executed in the user's browser.

Reflected XSS: The injected script is embedded in a URL or other input fields and is reflected back to the user by the server without proper sanitization. The script is executed in the victim's browser when they click on a malicious link or submit a form.

DOM-based XSS: This type of XSS occurs when the vulnerability is within the client-side JavaScript code, manipulating the Document Object Model (DOM) of a web page. The malicious script modifies the page's structure or behavior, leading to unexpected consequences and potential security risks.
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

