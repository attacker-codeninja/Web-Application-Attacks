
# insecure direct object references
## Summary
````
https://portswigger.net/web-security/access-control/idor
````
Insecure direct object references (IDOR) are a type of access control vulnerability that arises when an application uses user-supplied input to access objects directly. The term IDOR was popularized by its appearance in the OWASP 2007 Top Ten. However, it is just one example of many access control implementation mistakes that can lead to access controls being circumvented. IDOR vulnerabilities are most commonly associated with horizontal privilege escalation, but they can also arise in relation to vertical privilege escalation.

````
chatgpt
````
Insecure Direct Object References (IDOR): A direct object reference occurs when an application exposes a reference to an internal implementation object, such as a file or database record. If the application does not properly validate and enforce authorization checks on these references, an attacker may be able to manipulate the references and access unauthorized resources.

````
Explaining this to a 5th grader
````
Imagine you and your friends have a secret clubhouse with different rooms. Each room has a number on it, like Room 1, Room 2, and so on. You have a rule that says only certain friends are allowed to enter specific rooms.

Now, let's say you have a friend named Alex, and Alex is only allowed to enter Room 3. But one day, Alex figures out a way to sneak into Room 4, even though they are not supposed to be there. This is called an Insecure Direct Object Reference, or IDOR, because Alex directly accessed a room they were not authorized to enter.

In computer systems, IDOR happens when someone finds a way to access or modify information they are not supposed to have access to. It's like sneaking into a restricted area of a website or an application and seeing things that should be hidden.

To prevent IDOR, it's important for the computer system to have strong security measures. Just like your secret clubhouse needs a lock on each room to keep people out, computer systems need proper controls and checks to make sure that only authorized users can access the right information.

So, in simple terms, IDOR is when someone finds a way to access something they shouldn't be able to, just like sneaking into a restricted room in a secret clubhouse. It's important to have good security measures in place to protect against IDOR and keep things safe and private.
## Setup
````
docker build -t idor .
docker run -p 5000:5000 idor 
````
