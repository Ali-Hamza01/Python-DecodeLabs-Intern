#  Random Password Generator

A simple and secure **Random Password Generator** built with Python as part of **DecodeLabs Industrial Training — Project 3**.

The purpose of this project is to practice Python's built-in `random` and `string` modules, user input, loops, lists, string manipulation, and random character generation.

##  Project Objective

The program asks the user to enter a desired password length and generates a random password containing:

* Letters
* Numbers
* Special characters

The program also ensures that every generated password contains **at least one number and one special character**.

##  Technologies Used

* Python
* `random` module
* `string` module

##  Features

* User-defined password length
* Random uppercase and lowercase letters
* Random numbers
* Special characters such as `! @ # $ %  & *`
* At least one number is guaranteed
* At least one special character is guaranteed
* Randomly shuffles the generated password
* Minimum password length validation

##  Project Structure

```text
Project-3/
│
├── Password_Generator.py
└── README.md
```

##  Python Concepts Used

### 1. Importing Modules

```python
import random
import string
```

The `random` module is used to select random characters, while the `string` module provides predefined collections of letters and numbers.

### 2. String Constants

```python
letters = string.ascii_letters
numbers = string.digits
special_characters = "!@#$%&*"
```

`string.ascii_letters` provides uppercase and lowercase letters, while `string.digits` provides numbers from `0` to `9`.

### 3. User Input

```python
length = int(input("Enter password length: "))
```

The user enters the desired password length.

### 4. `random.choice()`

```python
random.choice(characters)
```

This selects one random character from the available characters.

### 5. `append()`

```python
password.append(random.choice(characters))
```

`append()` adds a new character to the end of the password list.

### 6. `join()`

```python
password = "".join(password)
```

The generated characters are initially stored in a list. `join()` combines those characters into one final password string.


##  Example

```text
Enter password length: 8
Generated Password: U7!Ol!FT
```

The generated password contains letters, numbers, and special characters.

##  Learning Outcome

Through this project, I practiced:

* Importing and using Python modules
* String manipulation
* Lists
* `append()`
* `join()`
* `for` loops
* Conditional statements
* User input
* Random character generation
* Password generation logic

##  Project Purpose

This project demonstrates how Python's built-in libraries can be integrated with basic programming logic to create a practical security-related tool.

##  Author

**Ali Hamza**

Python | Machine Learning | Data Science Enthusiast
