def trivia_quiz():
    # Define a dictionary with trivia questions and answers
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "What is the largest ocean on Earth?": "Pacific",
        "Who wrote 'Hamlet'?": "Shakespeare",
        "What planet is known as the Red Planet?": "Mars"
    }
    
    print("Welcome to the Trivia Quiz!")
    
    # Loop through the questions
    for question, correct_answer in questions.items():
        print(f"\nQuestion: {question}")
        user_answer = input("Your answer: ").strip()
        
        # Check if the user's answer is correct
        if user_answer.lower() == correct_answer.lower():
            print("Correct! Well done.")
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
    
    print("\nThank you for playing the Trivia Quiz!")

# Start the trivia quiz
trivia_quiz()