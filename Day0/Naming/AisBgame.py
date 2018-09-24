try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from questions import Question


class Application(tk.Frame):
    def __init__(self, master=None):
        self.total_questions = 0
        self.correct_questions = 0

        tk.Frame.__init__(self, master)

        self.pack()
        self.createWidgets()

        self.get_next_question()


    def createWidgets(self):

        self.new_question_box = tk.Button(self, text="Next Question", command=self.get_next_question, font=("Courier", 24))
        self.new_question_box.pack(side='right')

        self.false = tk.Button(self, text="False", command= lambda: self.answer_question(False), font=("Courier", 24))
        self.false.pack(side='right')

        self.true = tk.Button(self, text="True", command= lambda: self.answer_question(True), font=("Courier", 24))
        self.true.pack(side="right")

        self.text_box = tk.Label(text='This is where the question goes.', font=("Courier", 36))
        self.text_box.pack(side="bottom")
        print('made text box')


        self.feedback_box = tk.Label(text='Feedback Goes Here')
        self.feedback_box.pack(side="bottom")

        self.score_box = tk.Label(text='0 Correct of 0 Total')
        self.score_box.pack(side='bottom')

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy, font=("Courier", 24))
        self.QUIT.pack(side="right")

    def answer_question(self, answer):
        if not self.current_question.answered:
            self.current_question.answered = True

            feedback = {True: 'Correct!', False: 'Incorrect.'}
            correct = self.current_question.correct_answer == answer

            self.feedback_box['text'] = feedback[correct]
            self.correct_questions = self.correct_questions + 1 if correct else self.correct_questions
            self.score_box['text'] = "{} Correct of {} Total".format(self.correct_questions, self.total_questions)

    def get_next_question(self):
        self.total_questions += 1
        self.current_question = Question.get_random()
        self.text_box['text'] = self.current_question
        self.feedback_box['text'] = ''




root = tk.Tk()
root.title('a is b?')
app = Application(master=root)
app.mainloop()
