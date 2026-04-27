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

print("===== Quiz Questions =====")

for i in range(len(questions)):
    print(f"\nQ{i+1}. {questions[i]}")
    for opt in options[i]:
        print(opt)
