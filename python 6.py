import tkinter as tk
from tkinter import messagebox, Toplevel, simpledialog
import random
import time

class PaceApp:
    def __init__(self, master):
        self.master = master
        master.title("NASA PACE Mission App")

        self.frame = tk.Frame(master)
        self.frame.pack(padx=10, pady=10)

        self.start_button = tk.Button(self.frame, text="Learn About PACE and Start Quiz", command=self.start_intro)
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
            "Some cool facts about PACE:\n"
            "- Launched on February 8, 2024.\n"
            "- It uses special instruments to study tiny ocean plants called phytoplankton.\n"
            "- It can detect things like clouds and aerosols, which are tiny particles in the air.\n"
            "- PACE will help scientists monitor harmful algal blooms, which can be bad for marine life and people.\n\n"
            "Get ready to test your knowledge about PACE with a fun quiz!"
        )

        intro_label = tk.Label(self.intro_window, text=intro_text, justify="left", wraplength=400)
        intro_label.pack(padx=10, pady=10)

        self.ask_user_info()

    def ask_user_info(self):
        self.user_name = simpledialog.askstring("User Name", "What's your name?")
        self.user_age = simpledialog.askinteger("User Age", "What's your age?")

        start_quiz_button = tk.Button(self.intro_window, text="Start the Quiz!", command=self.start_quiz)
        start_quiz_button.pack(pady=10)

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
                "question": "What harmful event does PACE help monitor?",
                "options": [
                    "Harmful Algal Blooms", 
                    "Volcanic Eruptions", 
                    "Tornadoes",
                    "Alien Invasions"
                ],
                "answer": "Harmful Algal Blooms"
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
                "question": "What do aerosols in the atmosphere affect?",
                "options": [
                    "Weather and climate", 
                    "Pizza toppings", 
                    "Alien signals",
                    "Ocean depths"
                ],
                "answer": "Weather and climate"
            },
            {
                "question": "Which ocean color indicates high phytoplankton concentration?",
                "options": [
                    "Green", 
                    "Red", 
                    "Blue", 
                    "Yellow"
                ],
                "answer": "Green"
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
            },
            {
                "question": "What is the main purpose of the HARP2 instrument?",
                "options": [
                    "To make ice cream", 
                    "To monitor coastal waters", 
                    "To measure fish sizes",
                    "To check cloud shapes"
                ],
                "answer": "To monitor coastal waters"
            },
            {
                "question": "What does OCI stand for?",
                "options": [
                    "Ocean Color Instrument", 
                    "Oceanic Color Index", 
                    "Oceanic Climate Instrument",
                    "Oceans and Clouds Interceptor"
                ],
                "answer": "Ocean Color Instrument"
            },
            {
                "question": "How does PACE help with climate research?",
                "options": [
                    "By studying the Moon", 
                    "By monitoring ocean and atmospheric interactions", 
                    "By predicting superhero movies",
                    "By counting clouds"
                ],
                "answer": "By monitoring ocean and atmospheric interactions"
            },
            {
                "question": "What kind of data will PACE provide?",
                "options": [
                    "1.5 petabytes", 
                    "1.5 gigabytes", 
                    "1.5 terabytes",
                    "1.5 megabytes"
                ],
                "answer": "1.5 petabytes"
            },
            {
                "question": "Which of these is a benefit of studying phytoplankton?",
                "options": [
                    "Understanding carbon cycles", 
                    "Finding new pizza recipes", 
                    "Designing better video games",
                    "Building underwater cities"
                ],
                "answer": "Understanding carbon cycles"
            },
            {
                "question": "What color is often associated with healthy ocean ecosystems?",
                "options": [
                    "Bright green", 
                    "Dull brown", 
                    "Dark blue",
                    "Gray"
                ],
                "answer": "Bright green"
            },
            {
                "question": "What major event can be caused by harmful algal blooms?",
                "options": [
                    "Fish kills", 
                    "Rainbows", 
                    "Underwater concerts",
                    "Alien invasions"
                ],
                "answer": "Fish kills"
            },
            {
                "question": "Which instrument is used for hyperspectral imaging?",
                "options": [
                    "SPECIM", 
                    "HARP2", 
                    "OCI",
                    "Color Catcher"
                ],
                "answer": "SPECIM"
            },
            {
                "question": "What is the primary focus of the PACE mission?",
                "options": [
                    "Studying space rocks", 
                    "Exploring other planets", 
                    "Monitoring Earth's oceans and atmosphere",
                    "Inventing new flavors of ice cream"
                ],
                "answer": "Monitoring Earth's oceans and atmosphere"
            },
            {
                "question": "How does PACE contribute to environmental management?",
                "options": [
                    "By helping track ocean health", 
                    "By making weather forecasts", 
                    "By predicting video game trends",
                    "By inventing new sports"
                ],
                "answer": "By helping track ocean health"
            }
        ]
        
        random.shuffle(self.questions)
        self.current_question_index = 0
        self.score = 0
        self.start_time = time.time()

        self.quiz_window = Toplevel(self.master)
        self.quiz_window.title("PACE Quiz")
        self.display_question()

    def display_question(self):
        question_data = self.questions[self.current_question_index]
        self.quiz_window.title(f"Question {self.current_question_index + 1}")
        
        self.question_label = tk.Label(self.quiz_window, text=question_data['question'], wraplength=300)
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()  # No default value
        self.options_frame = tk.Frame(self.quiz_window)
        self.options_frame.pack(pady=10)

        self.option_buttons = []
        for option in question_data['options']:
            btn = tk.Radiobutton(self.options_frame, variable=self.var, text=option, value=option, command=self.check_answer)
            btn.pack(anchor='w')
            self.option_buttons.append(btn)

    def check_answer(self):
        if self.var.get() == "":
            return  # Do nothing if no option is selected
            
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
        total_time = time.time() - self.start_time
        motivation = "🌟 Remember, every great scientist started with questions just like you! Keep exploring and learning! 🌟"
        
        messagebox.showinfo("Quiz Complete", f"{self.user_name}, aged {self.user_age}:\nYour Score: {self.score}/{len(self.questions)}\nTotal Time: {total_time:.2f} seconds\n\n{motivation}")

        self.ask_for_feedback()

    def ask_for_feedback(self):
        feedback = simpledialog.askstring("Feedback", "What did you think of the quiz? Any suggestions?")
        if feedback:
            messagebox.showinfo("Thank You!", "Thank you for your feedback! 😊")

        self.show_smiley()

    def show_smiley(self):
        smiley_window = Toplevel(self.master)
        smiley_window.title("Smiley Face")
        smiley_label = tk.Label(smiley_window, text="😊", font=("Arial", 100))
        smiley_label.pack(padx=50, pady=50)

if __name__ == "__main__":
    root = tk.Tk()
    app = PaceApp(root)
    root.mainloop()
