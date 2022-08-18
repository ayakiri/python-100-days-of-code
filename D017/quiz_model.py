class QuizGame:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def print_question(self):
        print(f"Question {self.question_number + 1}: {self.question_list[self.question_number].question}")
        choice = input("True/False? ")
        self.check_answer(choice)

    def check_answer(self, choice):
        if choice.title() == self.question_list[self.question_number].correct_answer.title():
            print("You are right!")
            self.score += 1
        else:
            print("That's wrong!")
            print(f"The correct answer was {self.question_list[self.question_number].correct_answer}")
        self.question_number += 1
        print(f"Score: {self.score}/{self.question_number}\n")

    def print_outcome(self):
        print("==============================")
        print("You've completed the quiz")
        print(f"Your final score is {self.score}/{self.question_number}")
        print("==============================")


