# Created by Farhan for CodeLab II Portfolio

import tkinter as tk
from tkinter import messagebox

def analyze_text():
    text = text_entry.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Empty Text", "Please enter some text first!")
        return

    letters = sum(c.isalpha() for c in text)
    words = len(text.split())
    sentences = text.count('.') + text.count('!') + text.count('?')

    result_label.config(text=f"Letters: {letters}\nWords: {words}\nSentences: {sentences}")

# main window
window = tk.Tk()
window.title("Farhan's Text Analyzer")
window.geometry("400x300")
window.config(bg="#e0f7fa")

# title label
title = tk.Label(window, text="Farhan's Text Analyzer", font=("Arial", 16, "bold"), bg="#00acc1", fg="white", pady=10)
title.pack(fill="x")

# text box
text_entry = tk.Text(window, height=6, width=40, bg="#ffffff", fg="#000000", relief="solid", bd=1)
text_entry.pack(pady=10)

# analyze button
analyze_btn = tk.Button(window, text="Analyze", command=analyze_text, bg="#26c6da", fg="white", font=("Arial", 12, "bold"))
analyze_btn.pack(pady=5)

# result label
result_label = tk.Label(window, text="", font=("Arial", 12), bg="#e0f7fa", fg="#004d40")
result_label.pack(pady=10)

window.mainloop()