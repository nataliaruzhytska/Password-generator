# Password-generator
A simple password generating Flask app that can check your password in The Pwned Passwords API (https://haveibeenpwned.com/API/v3). 
The Pwned Passwords API is a service that check whether a password has been exposed as part of a number of numerous data breaches that have occurred several times in the past. These data contain more than 500,000,000 passwords that have been used before.

## API Endpoints
Authentication
> Registration:
```
POST
/register
```
> Log In:
```
POST
/login
```
> Log Out:
```
GET
http://localhost:5000/logout
```
>Password Generator:
```
POST
/
```
Generate a random password using user-defined parameters and evaluates its difficulty

> Password Storage:
```
GET
/save
```
Show stored password for user if user is login
```
POST
/save
```
Save password in database for user is login
```
DELETE
/save/<password_id>
```
Delete password from database for user is login

> Password Check:
```
GET
/check/<int:password_id>
```
Check password SHA1 hash in online hash base using api https://haveibeenpwned.com/API/v3


