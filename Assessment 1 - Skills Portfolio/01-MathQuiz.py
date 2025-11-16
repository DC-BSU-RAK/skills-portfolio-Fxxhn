import tkinter as tk
import random
from tkinter import messagebox

class MathsQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Maths Quiz")
        self.root.geometry("400x300")
        self.root.configure(bg="#D6EAF8")

        self.score = 0
        self.question_number = 0
        self.total_questions = 5

        self.title_label = tk.Label(root, text="Farhan's  Maths Quiz", 
                                    font=("Arial", 16, "bold"), 
                                    bg="#D6EAF8", fg="#154360")
        self.title_label.pack(pady=20)

        self.question_label = tk.Label(root, text="", 
                                       font=("Arial", 14), 
                                       bg="#D6EAF8", fg="#1B4F72")
        self.question_label.pack(pady=15)

        self.answer_entry = tk.Entry(root, font=("Arial", 12), justify="center",
                                     bg="#EBF5FB", fg="#154360")
        # Entry is hidden at first
        self.answer_entry.pack_forget()

        self.next_btn = tk.Button(root, text="Next", font=("Arial", 12, "bold"),
                                  bg="#48C9B0", fg="white", command=self.next_question)
        # Hidden until quiz starts
        self.next_btn.pack_forget()

        self.start_btn = tk.Button(root, text="Start Quiz", font=("Arial", 12, "bold"),
                                   bg="#43A047", fg="white", command=self.start_quiz)
        self.start_btn.pack(pady=30, ipadx=20, ipady=5)

        self.score_label = tk.Label(root, text="", 
                                    font=("Arial", 12, "bold"), 
                                    bg="#D6EAF8", fg="#117864")
        self.score_label.pack(pady=10)

    def start_quiz(self):
        self.start_btn.pack_forget()  
        self.answer_entry.pack(pady=10, ipadx=20, ipady=5)
        self.next_btn.pack(pady=15, ipadx=20, ipady=5)
        self.score_label.config(text="Score: 0")
        self.next_question()

    def next_question(self):
        if self.question_number > 0:
            user_ans = self.answer_entry.get()
            if user_ans.isdigit():
                if int(user_ans) == self.a + self.b:
                    self.score += 1
                    messagebox.showinfo("Correct", "Good job!")
                else:
                    messagebox.showwarning("Wrong", f"Answer was {self.a + self.b}")
            else:
                messagebox.showerror("Error", "Please type a number")
            self.score_label.config(text=f"Score: {self.score}")

        if self.question_number < self.total_questions:
            self.a = random.randint(1, 10)
            self.b = random.randint(1, 10)
            self.question_number += 1
            self.question_label.config(text=f"Q{self.question_number}: {self.a} + {self.b} = ?")
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Quiz Finished", f"Your Final Score: {self.score}/{self.total_questions}")
            self.root.destroy()

root = tk.Tk()
app = MathsQuiz(root)
root.mainloop()