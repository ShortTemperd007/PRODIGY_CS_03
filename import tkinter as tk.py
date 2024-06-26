import tkinter as tk
from tkinter import messagebox
import re

def assess_password_strength(password):
    length = len(password)
    score = 0
    
    # Criteria: Length
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1

    # Criteria: Presence of uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1

    # Criteria: Presence of lowercase letters
    if re.search(r'[a-z]', password):
        score += 1

    # Criteria: Presence of numbers
    if re.search(r'[0-9]', password):
        score += 1

    # Criteria: Presence of special characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1

    return score

def check_password():
    password = entry_password.get()
    strength_score = assess_password_strength(password)

    strength_feedback = ""
    if strength_score <= 2:
        strength_feedback = "Weak"
    elif strength_score <= 4:
        strength_feedback = "Medium"
    else:
        strength_feedback = "Strong"

    messagebox.showinfo("Password Strength", f"Password Strength: {strength_feedback}")

# Create main window
root = tk.Tk()
root.title("Password Strength Assessment Tool")

# Add ShortTemperd to the GUI output
title_label = tk.Label(root, text="🔒 Password Strength Assessment Tool by ShortTemperd 🔒", font=("Helvetica", 16, "bold"), pady=10) 
title_label.pack()

# Create label and entry for password
label_password = tk.Label(root, text="Enter your password:", font=("Helvetica", 12)) 
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*", font=("Helvetica", 12))  
entry_password.pack(pady=5)

# Create button to check password
button_check = tk.Button(root, text="Check Password Strength", command=check_password, font=("Helvetica", 12), bg="blue", fg="white", padx=10, pady=5)  
button_check.pack(pady=10)

# Start the GUI
root.mainloop()

# Code belongs to ShortTemperd007
