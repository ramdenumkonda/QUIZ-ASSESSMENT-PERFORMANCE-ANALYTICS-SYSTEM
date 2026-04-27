questions = [
    "What is the capital of India?",
    "5 + 3 = ?",
    "Which language is used for AI?"
]

options = [
    ["A) Mumbai", "B) Delhi", "C) Chennai", "D) Kolkata"],
    ["A) 6", "B) 7", "C) 8", "D) 9"],
    ["A) Python", "B) HTML", "C) CSS", "D) SQL"]
]

answers = ["B", "C", "A"]

def display_questions():
    for i in range(len(questions)):
        print(f"\nQ{i+1}. {questions[i]}")
        for opt in options[i]:
            print(opt)

def accept_answers():
    user_answers = []
    for i in range(len(questions)):
        ans = input("Enter Answer: ").strip().upper()
        user_answers.append(ans)
    return user_answers

def evaluate_quiz(user_answers):
    score = 0
    for i in range(len(answers)):
        if user_answers[i] == answers[i]:
            score += 1
    return score

print("===== Quiz Started =====")
display_questions()
user_answers = accept_answers()
score = evaluate_quiz(user_answers)

print("\n===== Result =====")
print(f"Score: {score}/{len(questions)}")
