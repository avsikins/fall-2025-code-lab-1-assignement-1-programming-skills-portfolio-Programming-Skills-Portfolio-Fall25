# Exercise 04: Primitive Quiz (10 Questions)
# This program quizzes the user on the capitals of 10 different countries.

quiz = [
    {"Question 1": "What is the capital of France?", "Answer": "Paris"},
    {"Question 2": "What is the capital of Austria?", "Answer": "Vienna"},
    {"Question 3": "What is the capital of Denmark?", "Answer": "Copenhagen"},
    {"Question 4": "What is the capital of Germany?", "Answer": "Berlin"},
    {"Question 5": "What is the capital of Ireland?", "Answer": "Dublin"},
    {"Question 6": "What is the capital of Netherlands?", "Answer": "Amsterdam"},
    {"Question 7": "What is the capital of Portugal?", "Answer": "Lisbon"},
    {"Question 8": "What is the capital of Romania?", "Answer": "Bucharest"},
    {"Question 9": "What is the capital of Spain?", "Answer": "Madrid"},
    {"Question 10": "What is the capital of Ukraine?" , "Answer": "Kyiv"}
]

# Loop through each question in the quiz
for item in quiz: 
    for question, answer in item.items(): 
        if question.startswith("Question"): 
            user_answer = input(f"{item[question]} ")
            if user_answer.strip().lower() == item["Answer"].lower(): # Case-insensitive comparison
                print("Correct!")
            else:
                print(f"Incorrect! The correct answer is {item['Answer']}.")
