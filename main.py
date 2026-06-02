# Film quiz for Hunt for the Wilderpeople

questions_data = [
    {
        "question": "What year did the film come out in NZ?",
        "options": ["A. 2010", "B. 2012", "C. 2017", "D. 2016"],
        "answer": "D"
    },
    {
        "question": "What was the name of the bush they filmed in?",
        "options": ["A. Waipoua Forest Trail", "B. Waitakere Ranges", "C. Karamatura Falls", "D. St Johns Bush Walk"],
        "answer": "B"
    },
    {
        "question": "What was the budget of the film?",
        "options": ["A. $3.4 million", "B. $5.6 million ", "C. $10 million", "D. $4.7 million"],
        "answer": "A"
    },
    {
        "question": "How much many did the movie gross globally in USD?",
        "options": ["A. $6 million", "B. $10 million ", "C. $30 million", "D. $13 million"],
        "answer": "C"
    },
    {
        "q`uestion": "What was the name of Rikki's dog?",
        "options": ["A. Tupac", "B. Pablo", "C. Boy", "D. 50 Cent"],
        "answer": "A"
    },
]



def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {q['answer']}.")

    print(f"\nQuiz completed! Your final score is {score}/{len(questions)}.")


if __name__ == "__main__":
    run_quiz(questions_data)