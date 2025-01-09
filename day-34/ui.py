import html, time, tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # set up GUI
        self.window = tk.Tk()
        self.window.title("Quiz Game")
        self.window.geometry("400x600")
        self.window.configure(background=THEME_COLOR, padx=10, pady=10)
        # score
        self.score = tk.Label(text="Score: 0", background=THEME_COLOR, foreground="white")
        self.score.grid(row=0, column=2, padx=10, pady=10)
        # question
        self.canvas = tk.Canvas(self.window, width=370, height=350, background="white", borderwidth=0)
        self.canvas.grid(row=1, column=0,  columnspan=3)
        self.question = self.canvas.create_text(185, 150, anchor=tk.CENTER, fill="black", text="Question", width=300)
        # buttons
        false_img = tk.PhotoImage(file="images/false.png")
        self.false = tk.Button(self.window, image=false_img, pady=20, command=self.mark_false)
        self.false.grid(row=2, column=0)
        true_img = tk.PhotoImage(file="images/true.png")
        self.true = tk.Button(self.window, image=true_img, pady=20, command=self.mark_true)
        self.true.grid(row=2, column=2)
        # quiz brain
        self.quiz_brain = quiz_brain
        self.display_next_question()


        self.window.mainloop()

    def update_score(self):
        self.score.configure(text=f"Score: {self.quiz_brain.score}")

    def display_next_question(self):
        if self.quiz_brain.still_has_questions():
            self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question, text=html.unescape(self.quiz_brain.current_question.text))
        else:
            self.true.config(state=tk.DISABLED)
            self.false.config(state=tk.DISABLED)
            self.canvas.itemconfig(self.question, text=f"""You've completed the quiz!
Final score: {self.quiz_brain.score}/{self.quiz_brain.question_number}""")

    def change_colour(self, result: bool):
        new_bg = "green" if result else "red"
        self.canvas.config(background=new_bg)
        self.window.update()
        time.sleep(.5)
        self.canvas.config(background="white")
        self.window.update()

    def process_answer(self, user_answer: bool):
        result = self.quiz_brain.check_answer(user_answer)
        self.change_colour(result)
        self.update_score()
        self.display_next_question()

    def mark_true(self):
        self.process_answer(True)

    def mark_false(self):
        self.process_answer(False)
