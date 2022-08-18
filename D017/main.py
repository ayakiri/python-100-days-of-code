from question_model import Question
from data import question_data
from quiz_model import QuizGame


question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizGame(question_bank)

while quiz.still_has_questions():
    quiz.print_question()

quiz.print_outcome()

