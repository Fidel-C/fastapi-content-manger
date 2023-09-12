 API backend for managing posts using FastAPI and Tortoise ORM(async) and uvicorn server. The project involves a role-based authorization with three main roles: Admin, Ordinary User, and Public. In the SQLite database, there are two users predefined:

COMMAND uvicorn main:app --reload

The database as at now contains posts and two users



Admin User:

Username: admin
Password: admin123
Privileges: Create, View, Update, Delete, and React to posts



Ordinary User:

Username: johndoe
Password: test123
Privileges: View and React to posts




Public:

Privileges: View posts (no ability to react to or update posts)


Also includes Oauth2 based authentication 

Includes Requets Throtting to a maximum of 10 requests per minute in base endpoint(/) and get_posts endpoint (/posts/) limiting and CSRF protection
Includes unit tests for the main endpoints in auth and posts subapps
Includes CSRF protection


content-app/
│
├── auth/
│   ├── models.py (Database models for authentication)
│   ├── crud.py (CRUD operations for authentication)
│   └── schemas.py (Pydantic schemas for authentication)
│
├── posts/
│   ├── models.py (Database models for posts)
│   ├── crud.py (CRUD operations for posts)
│   └── schemas.py (Pydantic schemas for posts)
│
├── main.py (Main FastAPI application file)
│
├── conftest.py (Configuration for pytest)
│
├── settings.py (Application configuration settings)
│
├── database.sqlite (SQLite database file)
│
├── test_auth.py (Unit tests for authentication)
│
├── test_posts.py (Unit tests for posts)
│
├── README.txt (Project README documentation)
│
├── .env (Environment configuration file)
│
├── utils/
│   └── rate_limiter.py (Utility for rate limiting)
│
└── requirements.txt (List of project dependencies)



Descriptions:

auth/models.py: Contains database models related to authentication, such as User models.

auth/crud.py: Implements CRUD (Create, Read, Update, Delete) operations for authentication, including user creation and retrieval.

auth/schemas.py: Contains Pydantic schemas for authentication, which define data structures for user input and output.

posts/models.py: Contains database models related to posts, including Post models.

posts/crud.py: Implements CRUD operations for managing posts, including creation, retrieval, and deletion of posts.

posts/schemas.py: Contains Pydantic schemas for posts, defining data structures for creating and displaying posts.

main.py: The main FastAPI application file where you define routes, middleware, and the main application instance.

conftest.py: Configuration for pytest, enabling unit tests for your application.

settings.py: Application configuration settings, including database configurations, security settings, and more.

database.sqlite: The SQLite database file where your application's data is stored.

test_auth.py: Unit tests specific to the authentication functionality.

test_posts.py: Unit tests for testing the posts management functionality.

README.txt: Documentation file providing information about your project, how to set it up, and how to use it.

.env: Environment configuration file for storing environment-specific settings or secrets.

utils/rate_limiter.py: A utility module for implementing rate limiting in your application.

requirements.txt: A file listing all project dependencies for easy installation using tools like pip.

This project structure allows you to organize your FastAPI CMS backend neatly, separating authentication and posts management concerns while also including necessary utilities and testing infrastructure.
This structure reflects your use of Tortoise ORM for async CRUD operations, async-pytest for pytest compatibility with Tortoise ORM, and FastAPI OAuth 2.0 for authentication. It maintains the separation of concerns between authentication and posts management, includes unit tests compatible with async-pytest, and provides a clear project organization.




