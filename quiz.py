import os
import time

port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    print("Run the program normally")

# Questions (dictionary format)
quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["A. 5", "B. 8", "C. 10", "D. 6"],
        "answer": "B"
    },
    {
        "question": "Who is the founder of Microsoft?",
        "options": ["A. Elon Musk", "B. Bill Gates", "C. Steve Jobs", "D. Mark Zuckerberg"],
        "answer": "B"
    }
]

score = 0

print("🎯 Welcome to the Quiz App!")
print("You have 10 seconds for each question ⏱️\n")

# Loop through questions
for q in quiz:
    print(q["question"])
    for option in q["options"]:
        print(option)

    start_time = time.time()
    answer = input("Enter your answer (A/B/C/D): ").upper()
    end_time = time.time()

    # Timer check
    if end_time - start_time > 10:
        print("⏰ Time's up!")
    elif answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is {q['answer']}")

    print("-" * 30)

# Final score
print(f"🏆 Your Score: {score}/{len(quiz)}")

# Result message
if score == len(quiz):
    print("🔥 Excellent!")
elif score >= 2:
    print("👍 Good Job!")
else:
    print("📚 Keep Practicing!")