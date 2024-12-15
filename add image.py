from tkinter import Tk, Label
from PIL import Image, ImageTk

root = Tk()
root.configure(bg='lightgray') 

try:
    image = Image.open("images/key_generation.png")  
    print("Image loaded successfully.")
    image = image.resize((300, 300), Image.Resampling.LANCZOS) 
    photo = ImageTk.PhotoImage(image)
    
    label = Label(root, image=photo)
    label.image = photo  # Keep a reference
    label.pack()

except FileNotFoundError:
    print("Error: Image not found.")
except Exception as e:
    print(f"An error occurred: {e}")

root.mainloop()
