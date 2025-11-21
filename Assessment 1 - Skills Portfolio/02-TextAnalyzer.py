# Created by Farhan for CodeLab II Portfolio

import tkinter as tk
from tkinter import messagebox

# This function runs when the user clicks the "Analyze" button
def analyze_text():
    # Get the text written by the user from the text box
    # "1.0" means start at line 1, character 0
    # tk.END means read until the very end
    text = text_entry.get("1.0", tk.END).strip()

    # If the user didn't type anything, show a warning message
    if not text:
        messagebox.showwarning("Empty Text", "Please enter some text first!")
        return

    # Count how many characters are letters (A–Z or a–z)
    letters = sum(c.isalpha() for c in text)

    # Count how many words there are (split by spaces)
    words = len(text.split())

    # Count sentences by checking '.', '!', and '?'
    sentences = text.count('.') + text.count('!') + text.count('?')

    # Display the results on the screen
    result_label.config(text=f"Letters: {letters}\nWords: {words}\nSentences: {sentences}")

# ------------------------ Main Window Setup ------------------------

# Create the main application window
window = tk.Tk()
window.title("Farhan's Text Analyzer")    # Window title
window.geometry("400x300")                # Window size (width x height)
window.config(bg="#e0f7fa")               # Background color

# Title label at the top of the window
title = tk.Label(window, 
                 text="Farhan's Text Analyzer", 
                 font=("Arial", 16, "bold"), 
                 bg="#00acc1", 
                 fg="white", 
                 pady=10)
title.pack(fill="x")

# Text box where the user types or pastes their text
text_entry = tk.Text(window, 
                     height=6, 
                     width=40, 
                     bg="#ffffff", 
                     fg="#000000", 
                     relief="solid", 
                     bd=1)
text_entry.pack(pady=10)

# Button that starts the text analysis
analyze_btn = tk.Button(window, 
                        text="Analyze", 
                        command=analyze_text, 
                        bg="#26c6da", 
                        fg="white", 
                        font=("Arial", 12, "bold"))
analyze_btn.pack(pady=5)

# Label where the results (letters/words/sentences) will appear
result_label = tk.Label(window, 
                        text="", 
                        font=("Arial", 12), 
                        bg="#e0f7fa", 
                        fg="#004d40")
result_label.pack(pady=10)

# Run the window so it stays open
window.mainloop()
