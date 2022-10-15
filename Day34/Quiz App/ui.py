from tkinter import *
from quiz import Quiz
THEME_COLOR = "#375362"

class UI:
    def __init__(self, quiz: Quiz):
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Quiz App')
        self.window.config(pady=30, padx=20, bg=THEME_COLOR)

        self.score_text = Label(text='Score: 0', bg=THEME_COLOR, fg='white', font=('Arial', 15))
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='Some random text', width=280, fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        true_img = PhotoImage(file='images/true.png')
        self.true_btn = Button(image=true_img, highlightthickness=0, command=lambda: self.get_answer('True'))
        self.true_btn.grid(row=2, column=0)
        false_img = PhotoImage(file='images/false.png')
        self.false_btn = Button(image=false_img, highlightthickness=0, command=lambda: self.get_answer('False'))
        self.false_btn.grid(row=2, column=1)
        self.next_question()


        self.window.mainloop()


    def next_question(self):
        if self.quiz.has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.end_quiz()

    # func to take user input and go to the next question
    def get_answer(self, user_answer):
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)
        print(f'Your answer: {user_answer}')
        print(self.quiz.questions[self.quiz.current_question-1])

        self.window.after(1000, self.next_question)


    def give_feedback(self, correct: bool):
        if correct:
            self.canvas.config(bg='green')
            self.quiz.increase_score()
        else:
            self.canvas.config(bg='red')

        self.canvas.itemconfig(self.question_text, fill='white')

        self.window.after(1000, self.reset_canvas)


    def reset_canvas(self):
        self.canvas.config(bg='white')
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        self.score_text.config(text=f'Score: {self.quiz.score}')


    def end_quiz(self):
        self.canvas.itemconfig(self.question_text,
                               text=f'You answered all questions\nFinal Score: {self.quiz.score}',
                               font=('Arial', 23, 'italic'))
        self.true_btn.config(state='disabled')
        self.false_btn.config(state='disabled')

