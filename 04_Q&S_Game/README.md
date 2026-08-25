# 🎯 Simple Quiz Game

A beginner-friendly **Python Quiz Game** that asks the user 3 questions and keeps track of their score. The program gives **+1 point for every correct answer** and displays the final score at the end.

This project was created to practice basic Python programming concepts, especially **If-Else logic and Variables**.

## 📌 Project Overview

The Quiz Game asks the player three questions. After each answer, the program checks whether the answer is correct or incorrect.

* ✅ Correct answer → **+1 point**
* ❌ Wrong answer → **0 points**
* 🏆 Final score is displayed after all questions

## 🛠️ Technologies Used

* **Python 3**
* `input()`
* `print()`
* Variables
* `if-else` statements
* String methods
* Basic arithmetic

## 🎮 How the Game Works

The game starts with a score of `0`.

```python
score = 0
```

The user is then asked three questions.

For each question, the program uses `if-else` to check the answer:

```python
if answer.lower() == "paris":
    print("Correct! +1 point")
    score += 1
else:
    print("Wrong! The correct answer is Paris.")
```

If the answer is correct, the score increases by 1.

At the end, the final score is displayed:

```python
print("Your final score is:", score, "/ 3")
```

## 🧠 Key Skills Practiced

### 1. Variables

A variable is used to store the player's score:

```python
score = 0
```

### 2. If-Else Logic

`if-else` is used to make decisions based on the user's answer.

```python
if answer == "7":
    score += 1
else:
    print("Wrong!")
```

### 3. User Input

The `input()` function allows the player to enter their answers:

```python
answer = input("What is the capital of France? ")
```

### 4. Score Counter

The score is increased whenever the player gives a correct answer:

```python
score += 1
```

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone YOUR_REPOSITORY_LINK
```

### Step 2: Open the Project Folder

```bash
cd quiz-game
```

### Step 3: Run the Python File

```bash
python quiz_game.py
```

## 💻 Example Output

```text
1. What is the capital of France? Paris
Correct! +1 point

2. Which language are we using to create this game? Python
Correct! +1 point

3. How many days are there in a week? 5
Wrong! The correct answer is 7.

Quiz Finished!
Your final score is: 2 / 3
```

## 📚 What I Learned

Through this project, I practiced:

* How to use variables
* How to take input from users
* How `if-else` statements work
* How to create a score counter
* How to compare user input with correct answers
* How to build a simple interactive Python program

## 🚀 Future Improvements

Some possible improvements for this project are:

* Add more questions
* Add multiple-choice questions
* Randomize the questions
* Add different difficulty levels
* Add a timer
* Store high scores
* Give different messages based on the final score

## 👨‍💻 Author

**Ali Hamza**

This project is part of my Python programming learning journey and practice with **Control Flow and Variables**.
