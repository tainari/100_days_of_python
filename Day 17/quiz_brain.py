import random
from data import question_data
class QuizBrain():
    def __init__(self):
        self.total_qs = 0
        self.correct_as = 0
        self.remaining_questions = question_data#[q for q in question_data]
        self.n_remaining_questions = len(self.remaining_questions)
        self.current_question = None
        self.current_answer = None

    def choose_question(self):
        question_number = random.randint(0, self.n_remaining_questions-1)
        question = self.remaining_questions.pop(question_number)
        self.total_qs += 1
        self.n_remaining_questions -= 1
        self.current_question = question['text']
        self.current_answer = question['answer']
        #return question

    def take_answer(self):
        while True:
            user_answer = input(f"Q.{self.total_qs}: {self.current_question} (True/False): ").lower()
            if user_answer in {"t","true"}:
                return "True"
            elif user_answer in {"f","false"}:
                return "False"
            else:
                print("Not a valid response. Try again.")

    def check_answer(self,user_answer):
        if user_answer == self.current_answer:
            print("You got it right!")
            self.correct_as += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {self.current_answer}")
        print(f"Your current score is: {self.correct_as}/{self.total_qs}\n\n")