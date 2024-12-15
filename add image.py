from tkinter import Tk, Label
from PIL import Image, ImageTk

root = Tk()
root.configure(bg='lightgray')  # Add a background color

try:
    # Correct image path
    image = Image.open("images/key_generation.png")  # Make sure this path is correct
    print("Image loaded successfully.")
    image = image.resize((300, 300), Image.Resampling.LANCZOS)  # Resize with LANCZOS filter
    photo = ImageTk.PhotoImage(image)
    
    # Display image on a label
    label = Label(root, image=photo)
    label.image = photo  # Keep a reference
    label.pack()

except FileNotFoundError:
    print("Error: Image not found.")
except Exception as e:
    print(f"An error occurred: {e}")

root.mainloop()
