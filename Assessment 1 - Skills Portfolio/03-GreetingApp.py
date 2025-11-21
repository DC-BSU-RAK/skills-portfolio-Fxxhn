import tkinter as tk
from tkinter import messagebox

# Function to greet the user when button is clicked
def greet_user():
    name = name_entry.get()  # Get the name from the entry box
    if name.strip():         # Check if the name is not empty
        messagebox.showinfo("Hello! 👋", f"Hello, {name}!\nWelcome to this app made by Farhan!")
    else:
        messagebox.showwarning("Warning ⚠️", "Please type your name")  # Show warning if empty

# ------------------------ Main Window Setup ------------------------

# Create the main window
root = tk.Tk()
root.title("Greeting App")         # Window title
root.geometry("450x300")           # Window size
root.configure(bg="#FFFDE7")       # Background color

# Title label at the top
title_label = tk.Label(root, 
                       text="🎉 Welcome to Farhan's Greeting App 🎉",
                       font=("Comic Sans MS", 16, "bold"),
                       bg="#FFECB3", fg="#BF360C", pady=10, relief="ridge", bd=2)
title_label.pack(fill="x", padx=10, pady=15)

# Instruction label for user
instruction_label = tk.Label(root, 
                             text="Enter your name below:",
                             font=("Arial", 14), bg="#FFFDE7", fg="#3E2723")
instruction_label.pack(pady=10)

# Entry box where user types their name
name_entry = tk.Entry(root, 
                      font=("Arial", 13, "bold"), justify="center",
                      bg="#FFE0B2", fg="#3E2723", bd=2, relief="solid")
name_entry.pack(pady=10, ipadx=40, ipady=5)

# Button to trigger greeting
greet_button = tk.Button(root, text="Greet Me! 🌟", command=greet_user,
                         font=("Arial", 12, "bold"), bg="#FF8A65", fg="white",
                         activebackground="#FF7043", activeforeground="white",
                         relief="raised", bd=3)
greet_button.pack(pady=20, ipadx=25, ipady=5)

# Footer decoration at the bottom
footer = tk.Frame(root, bg="#FFE082", height=30)
footer.pack(fill="x", side="bottom")

# Run the main event loop
root.mainloop()
