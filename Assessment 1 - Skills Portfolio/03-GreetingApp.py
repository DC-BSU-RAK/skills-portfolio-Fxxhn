import tkinter as tk
from tkinter import messagebox

def greet_user():
    name = name_entry.get()
    if name.strip():
        messagebox.showinfo("Hello! 👋", f"Hello, {name}!\nWelcome to the app!")
    else:
        messagebox.showwarning("Warning ⚠️", "Please type your name")

# Main window
root = tk.Tk()
root.title("Greeting App")
root.geometry("450x300")
root.configure(bg="#FFFDE7")  # Soft warm background

# Title
title_label = tk.Label(root, text="🎉 Welcome to Farhan's Greeting App 🎉",
                       font=("Comic Sans MS", 16, "bold"),
                       bg="#FFECB3", fg="#BF360C", pady=10, relief="ridge", bd=2)
title_label.pack(fill="x", padx=10, pady=15)

# Instruction
instruction_label = tk.Label(root, text="Enter your name below:",
                             font=("Arial", 14), bg="#FFFDE7", fg="#3E2723")
instruction_label.pack(pady=10)

# Entry box
name_entry = tk.Entry(root, font=("Arial", 13, "bold"), justify="center",
                      bg="#FFE0B2", fg="#3E2723", bd=2, relief="solid")
name_entry.pack(pady=10, ipadx=40, ipady=5)

# Greet button
greet_button = tk.Button(root, text="Greet Me! 🌟", command=greet_user,
                         font=("Arial", 12, "bold"), bg="#FF8A65", fg="white",
                         activebackground="#FF7043", activeforeground="white",
                         relief="raised", bd=3)
greet_button.pack(pady=20, ipadx=25, ipady=5)

# Footer decoration
footer = tk.Frame(root, bg="#FFE082", height=30)
footer.pack(fill="x", side="bottom")

root.mainloop()