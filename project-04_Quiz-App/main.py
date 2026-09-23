def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
            "answer": "C"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Mars", "B) Jupiter", "C) Saturn", "D) Neptune"],
            "answer": "B"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A) H2O", "B) O2", "C) CO2", "D) NaCl"],
            "answer": "A"
        }
    ]

    score = 0

    for index, q in enumerate(questions):
        print(f"Question {index + 1}: {q['question']}")

        for option in q['options']:
            print(f"- {option}")

        user_answer = input("Your answer (A, B, C, or D): ")

        if user_answer.strip().upper() == q['answer'][0].upper():
            print("Correct!\n")
            score += 1

        print(f"Your final score is: {score}/{len(questions)}")
        

run_quiz()