import json
import random
import os

def load_questions(file_path):
    # 从文件中加载问题数据
    with open(file_path, 'r') as file:
        questions_data = json.load(file)
    return questions_data

def load_or_create_wrong_questions(file_path):
    # 如果文件存在，则加载错题数据，否则创建一个空的错题列表
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            wrong_questions = json.load(file)
    else:
        wrong_questions = []
    return wrong_questions

def save_wrong_questions(file_path, wrong_questions):
    # 保存错题数据到文件
    with open(file_path, 'w') as file:
        json.dump(wrong_questions, file)

def select_questions(questions_data, num_questions):
    # 随机选择一定数量的问题
    selected_questions = random.sample(questions_data, num_questions)
    return selected_questions

def display_question(question):
    # 显示问题和选项
    print(f"\n{question['question']}")
    for i, option in enumerate(question['options'], start=1):
        print(f"{chr(64 + i)}. {option}")

def get_user_answer():
    # 获取用户输入的答案
    return input("Your answer(s) (Comma-separated, e.g., A, B): ").upper().split(',')

def display_correct_answer(question):
    # 显示正确答案
    correct_answers = ', '.join(question['correct_answers'])
    print(f"\nCorrect answer(s): {correct_answers}")

def main():
    questions_file_path = 'question.json'  # 问题文件路径，请更改为实际路径
    wrong_questions_file_path = 'wrong_questions.json'  # 错题文件路径，请更改为实际路径

    # 用户选择从问题文件还是错题文件获取问题
    source_choice = input("Choose the source for questions ('Q' for question file, 'W' for wrong questions file): ").upper()

    if source_choice == 'Q':
        source_file_path = questions_file_path
    elif source_choice == 'W':
        source_file_path = wrong_questions_file_path
    else:
        print("Invalid choice. Exiting.")
        return

    # 加载问题数据和错题数据
    questions_data = load_questions(source_file_path)
    wrong_questions = load_or_create_wrong_questions(wrong_questions_file_path)

    num_questions = int(input("Enter the number of questions you want to attempt: "))
    selected_questions = select_questions(questions_data, num_questions)

    for i, question in enumerate(selected_questions, start=1):
        display_question(question)
        user_answers = get_user_answer()

        if set(user_answers) != set(question['correct_answers']):
            # 如果回答错误，显示正确答案并将问题记录到错题列表中
            display_correct_answer(question)
            wrong_questions.append(question)
        else:
            # 如果回答正确，从错题列表中删除相应的问题
            print("\nCorrect! This question will be removed from the wrong questions list.")
            if question in wrong_questions:
                wrong_questions.remove(question)

    # 保存更新后的错题数据到文件
    save_wrong_questions(wrong_questions_file_path, wrong_questions)

    print("\nCongratulations! You have completed all questions.")

    # 显示错误的问题和答案
    if wrong_questions:
        print("\nWrong answers:")
        for question in wrong_questions:
            print(f"\n{question['question']}")
            display_correct_answer(question)
    else:
        print("All answers are correct. No questions in the wrong answers list.")

if __name__ == "__main__":
    main()
