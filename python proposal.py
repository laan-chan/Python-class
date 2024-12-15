import tkinter as tk
import random

class LikeMeApp:
    def __init__(self, master):
        self.master = master
        master.title("Do You Like Me?")

        self.label = tk.Label(master, text="Do you like me?")
        self.label.pack(pady=20)

        self.yes_button = tk.Button(master, text="Yes", command=self.like)
        self.yes_button.pack(side=tk.LEFT, padx=20)

        self.no_button = tk.Button(master, text="No", command=self.move_no_button)
        self.no_button.pack(side=tk.RIGHT, padx=20)

    def like(self):
        self.label.config(text="Yay! I'm glad to hear that!")
        self.yes_button.config(state=tk.DISABLED)
        self.no_button.config(state=tk.DISABLED)

    def move_no_button(self):
        screen_width = self.master.winfo_width()
        screen_height = self.master.winfo_height()
        x = random.randint(0, screen_width - 100)  
        y = random.randint(0, screen_height - 50)  
        self.no_button.place(x=x, y=y)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x200")  
    app = LikeMeApp(root)
    root.mainloop()
