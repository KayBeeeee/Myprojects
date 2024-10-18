#The Quiz is called True or False
#The user will be asked a list of questions
# If True:
#Score=+1
# If False:
#Score=+0
#At the end of the quiz, the user's final score will be displayed
#The user can choose to play again or exit the program
#The user can also view their previous scores


#The user can also add their own questions to the quiz

# List of questions and their corresponding answers
questions = [
    ["Python is a high-level programming language.", True],
    ["Python is an interpreted language.", True],
    ["Python is used for web development.", False],
    ["Python is used for data science.", False],
    ["Python is used for machine learning.", False]
]

# Function to run the quiz
def run_quiz():
    score = 0
    for question, answer in questions:
        user_answer = input(question + " (True/False) ").lower()
        if user_answer == "true" and answer:
            print("Correct!")
            score += 1
        elif user_answer == "false" and not answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print(f"Your final score is {score}/{len(questions)}")

# Function to view previous scores
def view_scores():
    # Code to retrieve and display previous scores
    pass

# Function to add a new question
def add_question():
    new_question = input("Enter a new question: ")
    new_answer = input("Enter the answer (True/False): ").lower()
    if new_answer == "true":
        new_answer = True
    elif new_answer == "false":
        new_answer = False
    else:
        print("Invalid answer. Question not added.")
        return
    questions.append([new_question, new_answer])
    print("Question added successfully!")

# Main menu
while True:
    print("Welcome to the True or False Quiz!")
    print("1. Play Quiz")
    print("2. View Previous Scores")
    print("3. Add a Question")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        run_quiz()
    elif choice == "2":
        view_scores()
    elif choice == "3":
        add_question()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")







    

    

