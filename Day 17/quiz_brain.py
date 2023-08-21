import random
class QuizBrain():
    def __init__(self,questions):
        self.questions = questions
        self.total_qs = 0
        self.correct_as = 0
        self.current_question = None

    def next_question(self):
        #question_number = random.randint(0, self.n_remaining_questions-1)
        self.current_question = self.questions.pop(0)
        self.total_qs += 1
        #return question

    def take_answer(self):
        while True:
            user_answer = input(f"Q.{self.total_qs}: {self.current_question.text} (True/False): ").lower()
            if user_answer in {"t","true"}:
                return "True"
            elif user_answer in {"f","false"}:
                return "False"
            else:
                print("Not a valid response. Try again.")

    def check_answer(self,user_answer):
        if user_answer == self.current_question.answer:
            print("You got it right!")
            self.correct_as += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {self.current_question.answer}")
        print(f"Your current score is: {self.correct_as}/{self.total_qs}\n\n")