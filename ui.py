from tkinter import *
from quiz_brain import QuizBrain
from data import question_data
import random
import html

THEME_COLOR = "#375362"
GREEN = "#7FB77E"
RED = "#EB4747"

FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # interface

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzer")
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.window.config(bg=THEME_COLOR, highlightthickness=0, padx=20, pady=20)
        self.q_text = self.canvas.create_text(150,
                                              125,
                                              text="Some Question Text",
                                              font=FONT,
                                              width=280,
                                              fill=THEME_COLOR)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Score label
        self.score = Label()
        self.score.config(text="Score: 0",
                          highlightthickness=0,
                          bg=THEME_COLOR,
                          font=FONT,
                          fg="white")

        self.score.grid(row=0, column=1)

        # correct button
        correct_photo = PhotoImage(file="images//true.png")
        self.correct_button = Button(image=correct_photo, highlightthickness=0, command=self.true)
        self.correct_button.grid(row=2, column=0)

        # wrong button
        wrong_photo = PhotoImage(file="images//false.png")
        self.wrong_button = Button(image=wrong_photo, highlightthickness=0, command=self.false)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.bye()

    def false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def update_score(self):
        self.score.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
            self.window.after(1000, self.get_next_question)
            self.update_score()
        else:
            self.canvas.config(bg=RED)
            self.window.after(1000, self.get_next_question)

    def bye(self):
        self.canvas.itemconfig(self.q_text, text=("You've completed the quiz\n\n"
                                                  f"Your final score is: {self.quiz.score}/{self.quiz.question_number}"),
                               width=310)
        self.correct_button.config(state="disabled")
        self.wrong_button.config(state="disabled")
