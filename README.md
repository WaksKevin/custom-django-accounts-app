# Custom User Management System in Django

- A prebuilt basic accounts app template for managing users.
- The email (in place of the username) and password are used for authentication
- Customize it to your liking.
- Avoid all the hassle of thinking from scratch how to go about creating, listing, updating, deleting users, and logging in and logging out.

- Remember to add the following lines in your settings.py file:

``` python

AUTH_USER_MODEL = "accounts.User"

LOGIN_URL = "/login/" # your login url

```
