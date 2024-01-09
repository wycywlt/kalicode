import json
import random

# Load JSON data from a file
with open('question.json', 'r') as file:
    questions_data = json.load(file)


def select_questions(num_questions):
    # Randomly select questions
    selected_questions = random.sample(questions_data, num_questions)

    # Record incorrect answers
    incorrect_answers = []

    # Display and answer questions
    for i, question in enumerate(selected_questions, start=1):
        print(f"\nQuestion {i}:\n{question['question']}")
        for j, option in enumerate(question['options'], start=1):
            print(f"{chr(64 + j)}. {option}")

        user_answers = input("Your answers (Comma-separated, e.g., A, B): ").upper().split(',')

        if set(user_answers) != set(question.get('correct_answers', [])):
            incorrect_answers.append((i, question['question'], question['options'], question['correct_answers']))

    return incorrect_answers


# Get user input for the number of questions
num_questions = int(input("Enter the number of questions you want to attempt: "))

# Get and display incorrect answers
incorrect_answers = select_questions(num_questions)

# Display incorrect question numbers and their correct answers
if incorrect_answers:
    print("\n您做错的题目:")
    for question_number, question, options, correct_answers in incorrect_answers:
        print(f"Question {question_number}: \n{question}:\n{options}\n Correct Answers: {', '.join(correct_answers)}")
else:
    print("\nCongratulations! All answers are correct.")
