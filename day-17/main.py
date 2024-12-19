from quiz_brain import QuizBrain

quiz_brain = QuizBrain()
while quiz_brain.have_more_questions:
    quiz_brain.ask_question()

print(f"Your final score was {quiz_brain.score}/{quiz_brain.questions_asked}")