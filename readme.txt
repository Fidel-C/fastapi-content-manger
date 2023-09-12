 API backend for managing posts using FastAPI and Tortoise ORM(async) and uvicorn server. The project involves a role-based authorization with three main roles: Admin, Ordinary User, and Public. In the SQLite database, there are two users predefined:

COMMAND uvicorn:app main

The database as at now contains
Admin User:

Username: admin
Password: admin123
Privileges: Create, View, Update, Delete, and React to posts
Ordinary User:

Username: johndoe
Password: test123
Privileges: View and React to posts
Public:

Privileges: View posts (no ability to react or update)
Also includes speed limiting and CSRF protection