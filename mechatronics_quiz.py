# MECHATRONICS QUIZ APPLICATION
# Created by:oladeinde abubakar korewafunmi

# Store questions, options, answers and explanations
questions = [
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Computer Processing User"
        ],
        "answer": 1,
        "explanation": "CPU means Central Processing Unit."
    },

    {
        "question": "Which language is used for programming?",
        "options": [
            "HTML",
            "Python",
            "CSS",
            "JPEG"
        ],
        "answer": 2,
        "explanation": "Python is a programming language."
    },

    {
        "question": "What does RAM stand for?",
        "options": [
            "Random Access Memory",
            "Read Access Machine",
            "Run All Memory",
            "Random Active Machine"
        ],
        "answer": 1,
        "explanation": "RAM means Random Access Memory."
    },

    {
        "question": "Which component detects physical changes?",
        "options": [
            "Monitor",
            "Sensor",
            "Keyboard",
            "Printer"
        ],
        "answer": 2,
        "explanation": "Sensors detect physical changes."
    },

    {
        "question": "Which device measures voltage?",
        "options": [
            "Voltmeter",
            "Thermometer",
            "Barometer",
            "Speedometer"
        ],
        "answer": 1,
        "explanation": "A voltmeter measures voltage."
    }
]


# Function to calculate grade
def calculate_grade(score):

    percentage = (score / len(questions)) * 100

    if percentage >= 80:
        grade = "A"

    elif percentage >= 70:
        grade = "B"

    elif percentage >= 60:
        grade = "C"

    elif percentage >= 50:
        grade = "D"

    else:
        grade = "F"

    return percentage, grade


# Main quiz function
def start_quiz():

    score = 0

    print("==============================")
    print("   MECHATRONICS QUIZ APP")
    print("==============================")

    name = input("Enter your name: ")

    print("\nWelcome", name)
    print("Answer the following questions.")

    # Loop through all questions
    for item in questions:

        print("\n" + item["question"])

        # Display answer options
        for number, option in enumerate(item["options"], 1):
            print(number, ".", option)

        # Get and validate user's answer
        while True:
            try:
                answer = int(input("Enter answer (1-4): "))

                if 1 <= answer <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")

            except ValueError:
                print("Invalid input! Enter a number.")

        # Check answer
        if answer == item["answer"]:

            print("Correct answer!")
            score += 1

        else:

            print("Wrong answer!")
            print("Correct answer:", item["options"][item["answer"] - 1])

            # Extra feature: explain the correct answer
            print("Explanation:", item["explanation"])

    # Calculate final result
    percentage, grade = calculate_grade(score)

    print("\n==============================")
    print("          QUIZ RESULT")
    print("==============================")

    print("Student:", name)
    print("Total Questions:", len(questions))
    print("Correct Answers:", score)
    print("Wrong Answers:", len(questions) - score)

    print("Percentage:", percentage, "%")
    print("Grade:", grade)

    if grade == "A":
        print("Excellent performance!")

    elif grade == "B":
        print("Very good performance!")

    elif grade == "C":
        print("Good performance!")

    elif grade == "D":
        print("You passed!")

    else:
        print("You need more practice!")

    # Extra feature: allow the user to retake the quiz
    again = input("\nDo you want to try again? (yes/no): ")

    if again.lower() == "yes":
        start_quiz()

    else:
        print("Thank you for using the Mechatronics Quiz App!")


# Start the application
start_quiz()