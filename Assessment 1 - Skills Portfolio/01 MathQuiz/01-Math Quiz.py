import tkinter as tk
from tkinter import messagebox
import random

class MathQuiz:
    def __init__(self, window):
        # main window setup
        self.window = window
        self.window.title("Farhan's Maths Quiz")
        self.window.geometry("450x350")
        self.window.config(bg="#e3f2fd")

        # variables to store quiz info
        self.score = 0
        self.q_num = 0
        self.total_q = 10
        self.try_num = 1
        self.level = ""

        # title label
        self.title = tk.Label(window, text="Farhan's Maths Quiz",
                              font=("Arial", 18, "bold"),
                              bg="#e3f2fd", fg="#0d47a1")
        self.title.pack(pady=10)

        # frame for menu (difficulty level)
        self.menu = tk.Frame(window, bg="#e3f2fd")
        self.menu.pack()

        # label for difficulty
        tk.Label(self.menu, text="Choose Difficulty",
                 font=("Arial", 14, "bold"),
                 bg="#e3f2fd", fg="#0d47a1").pack(pady=10)

        # buttons for difficulty levels
        tk.Button(self.menu, text="Easy (1 digit)", width=20,
                  bg="#4caf50", fg="white",
                  command=lambda: self.start("easy")).pack(pady=5)

        tk.Button(self.menu, text="Moderate (2 digits)", width=20,
                  bg="#42a5f5", fg="white",
                  command=lambda: self.start("moderate")).pack(pady=5)

        tk.Button(self.menu, text="Advanced (4 digits)", width=20,
                  bg="#8e44ad", fg="white",
                  command=lambda: self.start("advanced")).pack(pady=5)

        # quiz widgets hidden until quiz starts
        self.question = tk.Label(window, text="", font=("Arial", 16),
                                 bg="#e3f2fd", fg="#0d47a1")

        self.answer = tk.Entry(window, font=("Arial", 14),
                               bg="white", fg="black", justify="center")

        self.submit_btn = tk.Button(window, text="Submit",
                                    font=("Arial", 12, "bold"),
                                    bg="#00bfa5", fg="white",
                                    command=self.check)

        self.score_label = tk.Label(window, text="",
                                    font=("Arial", 12, "bold"),
                                    bg="#e3f2fd", fg="#1b5e20")

    # function to start quiz after choosing difficulty
    def start(self, level_name):
        self.level = level_name
        self.menu.pack_forget()  # hide difficulty menu

        # reset values for new quiz
        self.score = 0
        self.q_num = 0
        self.try_num = 1

        # show the quiz widgets now.
        self.question.pack(pady=15)
        self.answer.pack(pady=10, ipadx=20, ipady=5)
        self.submit_btn.pack(pady=10, ipadx=15)
        self.score_label.pack(pady=10)
        self.score_label.config(text="Score: 0")

        self.new_question()

    # function to create a new question
    def new_question(self):
        self.try_num = 1  # reset attempts

        # choose number difficulty range
        if self.level == "easy":
            low, high = 1, 9
        elif self.level == "moderate":
            low, high = 10, 99
        else:
            low, high = 1000, 9999

        # pick two numbers randomly
        self.a = random.randint(low, high)
        self.b = random.randint(low, high)

        # choose addition or subtraction
        self.op = random.choice(["+", "-"])

        # increase question counter
        self.q_num += 1

        # show question on screen
        self.question.config(text=f"Q{self.q_num}: {self.a} {self.op} {self.b} = ?")

        # clear the answer box
        self.answer.delete(0, tk.END)

    # function to check user answer
    def check(self):
        ans = self.answer.get()

        # if user didn't enter a number
        if not ans.strip().isdigit():
            messagebox.showerror("Error", "Enter a valid number.")
            return

        ans = int(ans)

        # calculate the correct answer
        if self.op == "+":
            right = self.a + self.b
        else:
            right = self.a - self.b

        # check if user answer is correct
        if ans == right:
            # give 10 points if first try, else 5
            if self.try_num == 1:
                points = 10
            else:
                points = 5

            self.score += points
            messagebox.showinfo("Correct", f"Nice! +{points} points")
            self.score_label.config(text=f"Score: {self.score}")

            # move to next question
            if self.q_num < self.total_q:
                self.new_question()
            else:
                self.finish()

        else:
            # if first attempt wrong
            if self.try_num == 1:
                self.try_num = 2
                messagebox.showwarning("Try Again", "Wrong! Try once more.")
            else:
                # second attempt wrong
                messagebox.showwarning("Incorrect",
                                       f"Correct answer: {right}")

                if self.q_num < self.total_q:
                    self.new_question()
                else:
                    self.finish()

    # function for finishing quiz
    def finish(self):
        msg = f"Your Score: {self.score} / 100\nPlay Again?"
        again = messagebox.askyesno("Finished!", msg)

        if again:
            # go back to menu
            self.question.pack_forget()
            self.answer.pack_forget()
            self.submit_btn.pack_forget()
            self.score_label.pack_forget()
            self.menu.pack()
        else:
            # close window
            self.window.destroy()


# run the quiz
root = tk.Tk()
app = MathQuiz(root)
root.mainloop()
