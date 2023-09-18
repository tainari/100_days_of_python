import datetime
import time, tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        # window setup
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, pady=20, padx=20)
        # score text
        self.score_label = tkinter.Label(text="Score: 0", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1, pady=20, padx=20)
        # question_text
        self.question_canvas = tkinter.Canvas(height=250, width=300, background="white")
        self.question_text = self.question_canvas.create_text(
            150,
            125,
            text="text",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=260
        )
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=20, padx=20)
        # true/false buttons
        true_image = tkinter.PhotoImage(file="images/true.png")
        false_image = tkinter.PhotoImage(file="images/false.png")
        self.true_button = tkinter.Button(image=true_image, command=self.answer_true)
        self.true_button.grid(row=2, column=0, pady=20, padx=20)
        self.false_button = tkinter.Button(image=false_image, command=self.answer_false)
        self.false_button.grid(row=2, column=1, pady=20, padx=20)
        # get first question
        self.show_next_question()
        # keep window open
        self.window.mainloop()

    def show_next_question(self):
        self.question_canvas.configure(background="white")
        if self.quiz_brain.still_has_questions():
            next_question = self.quiz_brain.next_question()
            self.question_canvas.itemconfig(self.question_text, text=next_question)
            self.true_button["state"] = tkinter.NORMAL
            self.false_button["state"] = tkinter.NORMAL
        else:
            self.question_canvas.itemconfig(
                self.question_text,
                text=f"End of quiz!\nYou got {self.quiz_brain.score} / {self.quiz_brain.question_number} right."
            )

    def report_answer(self, is_correct):
        if is_correct:
            # self.question_canvas["background"] = "green"
            self.question_canvas.configure(background="green")
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        else:
            self.question_canvas.configure(background="red")
        self.question_canvas.update()
        self.window.after(1000)
        self.show_next_question()

    def answer_true(self):
        self.true_button["state"] = tkinter.DISABLED
        self.false_button["state"] = tkinter.DISABLED
        is_correct = self.quiz_brain.check_answer("True")
        self.report_answer(is_correct)

    def answer_false(self):
        self.true_button["state"] = tkinter.DISABLED
        self.false_button["state"] = tkinter.DISABLED
        is_correct = self.quiz_brain.check_answer("False")
        self.report_answer(is_correct)
