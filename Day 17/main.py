from random import shuffle
from quiz_brain import QuizBrain
from question import Question
from data import question_data

question_bank = [Question(question["question"],question["correct_answer"]) for question in question_data]
shuffle(question_bank)

quiz = QuizBrain(question_bank)

while len(quiz.questions) > 0:
    quiz.next_question()
    user_answer = quiz.take_answer()
    quiz.check_answer(user_answer)

print("You've completed the quiz!")