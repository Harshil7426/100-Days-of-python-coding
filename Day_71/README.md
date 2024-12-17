## 👉 Day 71 Challenge
Today's challenge is to build a simple login system.

Your program should:

- Display a menu with the ability to add a user or login.
- 'Add' user should:
    - Ask for a username and password.
    - Create a new password and a randomly generated 4 digit salt.
    - Append the salt to the password and hash it.
    - Store the hash and the salt in a repl db with the username as the key.
- 'Login' should:
    - Get username and password input.
    - Display a success message if details are correct.
- This system should work with multiple users.