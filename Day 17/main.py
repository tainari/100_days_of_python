from quiz_brain import QuizBrain

quiz = QuizBrain()

while quiz.n_remaining_questions > 0:
    quiz.choose_question()
    user_answer = quiz.take_answer()
    quiz.check_answer(user_answer)

print("You've completed the quiz!")