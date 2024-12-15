import tkinter as tk
from tkinter import messagebox, Toplevel, simpledialog
import random

class PaceApp:
    def __init__(self, master):
        self.master = master
        master.title("Learn About NASA PACE Mission")

        self.frame = tk.Frame(master)
        self.frame.pack(padx=10, pady=10)

        self.start_button = tk.Button(self.frame, text="Start Learning About PACE!", command=self.start_intro)
        self.start_button.pack(pady=5)

        self.quit_button = tk.Button(self.frame, text="Quit", command=master.quit)
        self.quit_button.pack(pady=5)

    def start_intro(self):
        self.intro_window = Toplevel(self.master)
        self.intro_window.title("Introduction to NASA PACE Mission")

        intro_text = (
            "Welcome to the NASA PACE Mission!\n\n"
            "PACE stands for Plankton, Aerosol, Cloud, ocean Ecosystem. It helps us understand "
            "how our oceans and atmosphere work together, especially in how they affect climate.\n\n"
            "Here are some cool facts about PACE:\n"
            "- Launched on February 8, 2024.\n"
            "- It studies tiny ocean plants called phytoplankton.\n"
            "- Uses advanced instruments to detect clouds and aerosols.\n"
            "- Helps monitor harmful algal blooms.\n\n"
            "Are you ready to test your knowledge with a fun quiz?"
        )

        intro_label = tk.Label(self.intro_window, text=intro_text, justify="left", wraplength=400)
        intro_label.pack(padx=10, pady=10)

        start_quiz_button = tk.Button(self.intro_window, text="Start Quiz!", command=self.start_quiz)
        start_quiz_button.pack(pady=10)

        fun_facts_button = tk.Button(self.intro_window, text="Show Fun Facts", command=self.show_fun_facts)
        fun_facts_button.pack(pady=10)

    def show_fun_facts(self):
        fun_facts = [
            "1. Phytoplankton produce about half of the world's oxygen!",
            "2. The ocean absorbs carbon dioxide from the atmosphere.",
            "3. NASA uses satellites to collect data on ocean health.",
            "4. PACE will generate about 1.5 petabytes of data!",
            "5. Understanding oceans helps predict climate change."
        ]
        selected_fact = random.choice(fun_facts)
        messagebox.showinfo("Fun Fact", selected_fact)

    def start_quiz(self):
        self.questions = [
            {
                "question": "What does PACE stand for?",
                "options": [
                    "Plankton, Aerosol, Cloud, ocean Ecosystem", 
                    "Pizza, Apples, Candy, and Eggplant", 
                    "Planetary Analysis of Climate and Ecosystems",
                    "Phytoplankton, Algae, Clouds, and Ecosystems"
                ],
                "answer": "Plankton, Aerosol, Cloud, ocean Ecosystem"
            },
            {
                "question": "What tiny ocean plants does PACE study?",
                "options": [
                    "Seaweed", 
                    "Coral", 
                    "Phytoplankton", 
                    "Jellyfish"
                ],
                "answer": "Phytoplankton"
            },
            {
                "question": "Which instrument measures ocean color in PACE?",
                "options": [
                    "The Ocean Color Instrument (OCI)", 
                    "The Fun Color Machine", 
                    "The Rainbow Detector",
                    "The Sea Color Picker"
                ],
                "answer": "The Ocean Color Instrument (OCI)"
            },
            {
                "question": "When was PACE launched?",
                "options": [
                    "February 8, 2024", 
                    "January 1, 2022", 
                    "December 31, 2025",
                    "March 15, 2023"
                ],
                "answer": "February 8, 2024"
            },
            {
                "question": "What is a common cause of harmful algal blooms?",
                "options": [
                    "Nutrient pollution", 
                    "Underwater volcanoes", 
                    "Space dust",
                    "Magic spells"
                ],
                "answer": "Nutrient pollution"
            }
        ]

        random.shuffle(self.questions)
        self.current_question_index = 0
        self.score = 0

        self.quiz_window = Toplevel(self.master)
        self.quiz_window.title("PACE Quiz")
        self.display_question()

    def display_question(self):
        question_data = self.questions[self.current_question_index]
        self.quiz_window.title(f"Question {self.current_question_index + 1}")
        
        self.question_label = tk.Label(self.quiz_window, text=question_data['question'], wraplength=300)
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.options_frame = tk.Frame(self.quiz_window)
        self.options_frame.pack(pady=10)

        self.option_buttons = []
        for option in question_data['options']:
            btn = tk.Radiobutton(self.options_frame, variable=self.var, text=option, value=option, command=self.check_answer)
            btn.pack(anchor='w')
            self.option_buttons.append(btn)

    def check_answer(self):
        question_data = self.questions[self.current_question_index]
        
        if self.var.get() == question_data['answer']:
            self.score += 1
            messagebox.showinfo("Result", "✅ Awesome! That's correct!")
        else:
            messagebox.showinfo("Result", f"❌ Not quite right! The correct answer was: {question_data['answer']}.")

        self.next_question()

    def next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.question_label.destroy()
            self.options_frame.destroy()
            self.display_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        messagebox.showinfo("Quiz Complete", f"Your Score: {self.score}/{len(self.questions)}\nThanks for participating! Keep learning about our planet!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaceApp(root)
    root.mainloop()
