# Python Remote Internship at DecodeLabs
# Assignment-04

score = 0

# Question-01
answer = input("1. What is the Capital of Pakistan?")

if answer.lower() == "islamabad":
    print("Correct +1 point")
    score += 1

else:
    print("Your answer is wrong.islamabad is correct answer.")




# Question-02

answer = input("2. which language are you using to create this game?")

if answer.lower() == "python":
    print("Correct +1 point.")
    score += 1

else:
    print("Wrong. Correct answer is python.")


# Question-03

answer = input("3. How many days are there in a week?")

if answer.lower() == "seven":
    print("Correct +1 point.")
    score += 1

else:
    print("Wrong. Correct answer is seven.")


# print Final Score
print("\n Quiz Finished")
print(f"Your Final Score is {score}/3")