from question_model import Question
from data import question_data

import random

class QuizBrain:
    def __init__(self):
        self.score = 0
        self.questions_asked = 0
        self.question_list = []
        for q in question_data:
            question = Question(q['text'], q['answer'].lower() == "true")
            self.question_list.append(question)
        random.shuffle(self.question_list)
        self.have_more_questions = len(self.question_list) > 0

    def ask_question(self):
        current_question = self.get_question()
        if current_question:
            q = current_question.question
            a = current_question.answer
            user_answer = self.get_answer(q)
            self.check_answer(user_answer, a)

    def get_question(self):
        if len(self.question_list) == 0:
            print("\nYou've finished all the questions!")
            self.have_more_questions = False
            return
        # Get a question to ask
        self.questions_asked += 1
        return self.question_list.pop()

    def get_answer(self, q):
        answer = input(f"Q{self.questions_asked}. {q}. True or False? ")
        return answer.lower()[0] == "t"

    def check_answer(self, user_answer, answer):
        if user_answer == answer:
            self.score += 1
            print("You got it right!")
        else:
            print("Sorry, that's wrong.")
        print(f"The answer was {answer}.")
        print(f"Your current score is {self.score}/{self.questions_asked}\n")