questions = (
    "How much is a byte equal to?:",
    "What is also known as portable computer?:",
    "Which one of the following is not operating system?:",
    "What memory below is the largest?:",
    "What do you need to use to connect to the internet?")

options = (("A. 8 bits ", "B. 16  bits ", "C. 32 bits ","D. 64 bits "),
            ("A. Laptop", "B. CPU ", "C. Monitor","D. Desktop"),
            ("A. Window 10", "B. Linux", "C. DOS","D. Ms Excel"),
            ("A. 1 GB", "B. 1 TB", "C. 55000 Bytes","D. 10GB"),
            ("A. Mouse", "B. Modem", "C. CPU","D. Keyboard"))
answers = ("A","A", "D","B","B")
guesses = []
score = 0
question_num = 0
for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")    
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-----------------")
print("     RESULTS        ")
print("-----------------")

print("answers: ",end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
