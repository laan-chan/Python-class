import tkinter as tk
from tkinter import messagebox

def check_eligibility():
    name = name_entry.get()
    age = int(age_entry.get())
    id_number = id_entry.get()
    place_of_birth = birth_entry.get()

    if age >= 18:
        if age <= 95:
            eligibility = f"{name}, you are eligible to vote and drive."
        else:
            eligibility = f"{name}, you are eligible to vote but not to drive."
    else:
        eligibility = f"{name}, you are not eligible to vote or drive."

    feedback = messagebox.askquestion("Feedback", "Would you like to provide feedback?")
    if feedback == 'yes':
        feedback_input = feedback_entry.get()
    else:
        feedback_input = "No feedback given."

    summary = (f"--- Summary of Your Information ---\n"
               f"Name: {name}\n"
               f"Age: {age}\n"
               f"ID Number: {id_number}\n"
               f"Place of Birth: {place_of_birth}\n"
               f"Feedback: {feedback_input}")
    
    messagebox.showinfo("Summary", summary)
    thank_user()

def thank_user():
    messagebox.showinfo("Thank You!", "Thank you for using our software!")

root = tk.Tk()
root.title("Eligibility Checker")
root.geometry("400x400")

tk.Label(root, text="Enter your name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Enter your age:").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Enter your ID number:").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Enter your place of birth:").pack()
birth_entry = tk.Entry(root)
birth_entry.pack()

tk.Label(root, text="Enter your feedback:").pack()
feedback_entry = tk.Entry(root)
feedback_entry.pack()

submit_button = tk.Button(root, text="Check Eligibility", command=check_eligibility)
submit_button.pack(pady=20)

root.mainloop()
