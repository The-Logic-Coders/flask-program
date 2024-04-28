# Lesson 0: Introduction to Flask and Setting Up the Development Environment 

## Learning Objectives
- Understand what Flask framework is and what it's used for.
- Set up the python development environment for Flask.
- Understand the basic structure and components of a Flask application.

## What is Flask?
Flask is a lightweight and flexible web framework for Python. It’s designed to make getting started with web development quick and easy, while still being powerful enough to build complex web applications.

## How to set up the Flask application

### Step 1: Install Flask
In Windows, at the Visual Studio Code terminal, type: 
```bash
pip install Flask
```

### Step 2: Clone Project Directory 
Get the initial setup files for the Flask application and navigate to the appropriate lesson directory:

**Instructions:**

In the terminal of Visual Studio Code, type the following command to clone the repository:
```bash
git clone https://github.com/The-Logic-Coders/flask-program.git
```
Change into the cloned project directory:
```bash
cd flask-program
```
Navigate to the Lesson 0 directory and then to the python code examples:
```bash
cd Lesson-0/python-code-examples
```
### Step 3: Test Flask
Verify that flask and the project setup are correctly configured.

Still in the Visual Studio Code terminal, and ensuring you are in the correct directory (`flask-program/Lesson-0/python-code-examples`), execute the Flask application with the following command:

```bash
python3 hello.py
```

Open a web browser (Google Chrome) and go to `localhost:5000/` to see if the Flask application is running correctly. If it is running correctly, you'll see something like this:

<img width="700" alt="ss1" src="https://github.com/The-Logic-Coders/flask-program/assets/115064816/7acc2d08-08f2-4774-a8d4-8c9c8cab74c4">
<img width="700" alt="ss1" src="https://github.com/The-Logic-Coders/flask-program/assets/115064816/53fb57a8-7acd-4abb-98ac-ebe35cb178b7">

## Basic Structure and Components of a Flask application

Deconstruct the code in `hello.py`

### Import Flask and create an application object

We begin here, with two lines you will see in every Flask app:

```python
from flask import Flask
app = Flask(__name__)
```
**The first line** is a typical Python import statement. Lowercase flask is a Python library, which you have installed. Uppercase Flask is a class from that library, and it must be imported

**The second line**, begins with a variable `app`, which will be used in every Flask application. The value of this variable, `Flask(__name__)`, is a new object that inherits from the clask Flask - meaning it gets all the attributes and methods built into the class.

`app = Flask(__name__)` creates a Flask application object — `app` — in the current Python module. An object  is a data type includes functions, methods, and attributes. Our variable `app` now has all of those from Flask. To be specific, app is an instance of a Python class named Flask, which we imported at the top of the file.

Basically, we have brought into this file — this `app` — all the *capabilities* of Flask.

### The Decorator

- A decorator begins with `@` and is a unique feature of the Python language. It modifies the function that follows it.  
- This decorator specifies the URL endpoint. In this case, `/` represents the root URL. This means that the decorated function will be called when a request is made to the root URL of the application.
- Recall that `app` is a Flask application object. It has all the methods and attributes of the Flask class, and one of those is `route()` which is used to assign a URL rule for a specific function.

``` python
@app.route('/')
```

### The Function
``` python
def hello():
    return 'Hello World!'
```
All this function does is return a simple string: 'Hello World!' Our Flask app performs this action when the server is running, the app is running, and we open `localhost:5000` in the browser. 

With these steps, you're all set up to start with a simple Flask application.

> Reference: Always refer to the [Flask Documentation](https://python-adv-web-apps.readthedocs.io/en/latest/flask.html) when in doubt.




