# Fastapi Template

A basic template to help kickstart development of a Fastapi based API. ideal for ideating and POCs, ready to grow with you. This template is completely front-end independent
and leaves all related decisions up to the developer.

## Features

* Minimal Fastapi app
* Async/Await Functionality
* JWT based OAuth security on a per endpoint basis
* Unit tests
* Type hints
* Basic Database Functionality Included (SQLite3)
* Support for .env

### Application Structure

The API is divided in three parts `users`, `posts` and `auth`.

The `users` part is responsible for all the routes associated with user management.

The `posts` part is responsible for handeling all requests related to adding, retrieving and deleting posts.

The `auth` part is responsible for handeling user registration and login. The login is Oauth2 based and uses JWTs.

## Installation

### Template and Dependencies

* Clone this repository:

 ```zsh
 git clone https://github.com/StefanVDWeide/fastapi-api-template.git
 ```

### Virtual Environment Setup

It is preferred to create a virtual environment per project, rather then installing all dependencies of each of your
projects system wide. Once you install [virtual env](https://virtualenv.pypa.io/en/stable/installation/), and move to
your projects directory through your terminal, you can set up a virtual env with:

```bash
python3 -m venv .venv
```

### Dependency installations

To install the necessary packages:

```bash
source venv/bin/activate
pip3 install -r requirements.txt
```

This will install the required packages within your venv.

---

### Setting up a SQLite3 Database

Database migrations are handled through Alembic. Migrations are for creating and uprading necessary tables in your database. The files generate by the migrations should be added to source control.

To setup a SQLite3 database for development (SQLite3 is usually **not** recommended for production unless you know what you are doing, use something like PostgreSQL or MySQL) navigate to the root folder and complete the following steps:

First, we need to initialize the database. Make sure you have a `.env` file in the root of the project with the following content:

```env
DATABASE_URL = sqlite+aiosqlite:///sql_app.db
DATABASE_TEST_URL = sqlite+aiosqlite:///test.db
JWT_SECRET_KEY = secret
JWT_REFRESH_SECRET_KEY = secret
```

Now that the app knows we want to use a SQLite database, run the following command to create it:

```zsh
alembic upgrade head
```

Finaly, run the API itself with the following command:

```zsh
uvicorn app.main:app --reload
```
