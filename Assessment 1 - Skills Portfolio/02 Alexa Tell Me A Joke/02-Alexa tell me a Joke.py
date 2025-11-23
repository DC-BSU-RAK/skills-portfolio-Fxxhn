import tkinter as tk
from tkinter import messagebox
import random


# Load jokes from the text file
jokes = []  # List to store all jokes
try:
    with open("Assessment 1 - Skills Portfolio/02 Alexa Tell Me A Joke/randomJokes.txt", "r") as f:  # Open the file in read mode
        for line in f:
            line = line.strip()  # Remove extra spaces
            if line:  # Skip empty lines
                jokes.append(line)  # Add joke to the list
except:
    messagebox.showerror("Error", "randomJokes.txt not found!")  # Show error if file missing

current_joke = None  # Store the currently displayed joke

# Functions
def new_joke():
    """Pick a new random joke and display the setup"""
    global current_joke
    if not jokes:  # Check if jokes list is empty
        messagebox.showinfo("No Jokes", "No jokes found!")
        return
    current_joke = random.choice(jokes)  # Pick a random joke
    if "?" in current_joke:
        setup, punch = current_joke.split("?", 1)  # Split joke into setup and punchline
        joke_label.config(text=setup + "?")  # Show setup
        punchline_label.config(text="")      # Clear previous punchline
    else:
        joke_label.config(text=current_joke)
        punchline_label.config(text="")

def show_punchline():
    """Show the punchline of the current joke"""
    global current_joke
    if not current_joke:  # Make sure a joke has been picked
        messagebox.showwarning("Oops", "Click 'Alexa tell me a Joke' first!")
        return
    if "?" in current_joke:
        setup, punch = current_joke.split("?", 1)
        punchline_label.config(text=punch.strip())  # Show punchline
    else:
        punchline_label.config(text="No punchline found!")


# Main Window
root = tk.Tk()
root.title("Alexa Joke App")  # Window title
root.geometry("500x350")      # Window size
root.configure(bg="#FFFDE7")  # Soft background color

# Title Label
title_label = tk.Label(root, text="😂 Farhan's Alexa Joke App 😂",
                       font=("Comic Sans MS", 16, "bold"),
                       bg="#FFECB3", fg="#BF360C", pady=10, relief="ridge", bd=2)
title_label.pack(fill="x", padx=10, pady=15)

# Joke setup label
joke_label = tk.Label(root, text="", font=("Arial", 14, "bold"),
                      bg="#FFFDE7", fg="#3E2723", wraplength=450, justify="center")
joke_label.pack(pady=20)

# Punchline label
punchline_label = tk.Label(root, text="", font=("Arial", 13),
                           bg="#FFFDE7", fg="#BF360C", wraplength=450, justify="center")
punchline_label.pack(pady=10)

# Buttons frame
btn_frame = tk.Frame(root, bg="#FFFDE7")
btn_frame.pack(pady=15)

# Buttons for user actions
tk.Button(btn_frame, text="Alexa tell me a Joke 🎤", command=new_joke,
          bg="#FF8A65", fg="white", font=("Arial", 12, "bold"), width=20).grid(row=0, column=0, padx=5, pady=5)

tk.Button(btn_frame, text="Show Punchline 😆", command=show_punchline,
          bg="#42a5f5", fg="white", font=("Arial", 12, "bold"), width=20).grid(row=1, column=0, padx=5, pady=5)

tk.Button(btn_frame, text="Next Joke ➡️", command=new_joke,
          bg="#4caf50", fg="white", font=("Arial", 12, "bold"), width=20).grid(row=2, column=0, padx=5, pady=5)

tk.Button(btn_frame, text="Quit ❌", command=root.destroy,
          bg="#e53935", fg="white", font=("Arial", 12, "bold"), width=20).grid(row=3, column=0, padx=5, pady=5)

# Run the app
root.mainloop()
