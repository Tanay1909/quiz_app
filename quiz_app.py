import random

# Define a class for the Quiz
class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question, options, correct_option):
        """Add a question to the quiz."""
        self.questions.append({
            "question": question,
            "options": options,
            "correct_option": correct_option
        })

    def start(self):
        """Start the quiz."""
        print("\nWelcome to the Quiz Application!")
        print("Answer the following questions:\n")
        
        for i, q in enumerate(self.questions, 1):
            print(f"Question {i}: {q['question']}")
            shuffled_options = q['options']
            random.shuffle(shuffled_options)

            # Display options
            for idx, option in enumerate(shuffled_options, 1):
                print(f"{idx}. {option}")

            # Get user's answer
            while True:
                try:
                    user_choice = int(input("Enter your choice (1-4): "))
                    if 1 <= user_choice <= len(shuffled_options):
                        break
                    else:
                        print("Invalid input. Please choose a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 4.")

            # Check answer
            if shuffled_options[user_choice - 1] == q["correct_option"]:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {q['correct_option']}\n")

        # Display final score
        print(f"You've completed the quiz! Your final score is {self.score}/{len(self.questions)}.")
        print("Thank you for playing!")

# Example Usage
if __name__ == "__main__":
    quiz = Quiz()

    # Add questions
    quiz.add_question(
        "What is the capital of France?",
        ["Paris", "Berlin", "Madrid", "Rome"],
        "Paris"
    )
    quiz.add_question(
        "Who wrote 'Pride and Prejudice'?",
        ["Jane Austen", "Mark Twain", "Charles Dickens", "Virginia Woolf"],
        "Jane Austen"
    )
    quiz.add_question(
        "Which planet is known as the Red Planet?",
        ["Earth", "Mars", "Jupiter", "Venus"],
        "Mars"
    )
    quiz.add_question(
        "What is the chemical symbol for water?",
        ["H2O", "O2", "CO2", "HO"],
        "H2O"
    )
    quiz.add_question(
       " Who is known as the Father of the Indian Constitution?",
        [ "Jawaharlal Nehru","B.R Ambedkar","Mahatma Gandhi","Sardar Vallabhbhai Patel"],
        "B.R. Ambedkar"
    )
    quiz.add_question(
       " Who was the first Indian to receive the Bharat Ratna Award?",
        [ 'Mahatma Gandhi','Dr. B.R. Ambedkar','Dr. Sarvepalli Radhakrishnan','C.V. Raman'],
        'C.V. Raman'
    )
    
    quiz.add_question(
        "The Davis Cup is associated with which sport?",
        [ " Football","Badminton","Tennis","Cricket"],
        " Tennis"
    )

    # Start the quiz
    quiz.start()
