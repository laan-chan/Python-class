from gettext import install

import pip

import tkinter as tk
from tkinter import messagebox
import pyperclip   # type: ignore

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 2
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def string_to_numbers(text):
    return [ord(char) for char in text]

def numbers_to_string(numbers):
    return ''.join(chr(num) for num in numbers)

def encrypt_string(message, public_key):
    numbers = string_to_numbers(message)
    return [pow(num, public_key[0], public_key[1]) for num in numbers]

def decrypt_string(ciphertext, private_key):
    numbers = [pow(num, private_key[0], private_key[1]) for num in ciphertext]
    return numbers_to_string(numbers)

def handle_encrypt():
    message = message_entry.get()
    if not message:
        messagebox.showerror("Input Error", "Please enter a message to encrypt.")
        return
    ciphertext = encrypt_string(message, public_key)
    encrypted_output.set(f"{ciphertext}")

def handle_decrypt():
    ciphertext_text = message_entry.get()
    if not ciphertext_text:
        messagebox.showerror("Input Error", "Please enter a ciphertext to decrypt.")
        return
    try:
        ciphertext = eval(ciphertext_text)  
        decrypted_message = decrypt_string(ciphertext, private_key)
        decrypted_output.set(f"{decrypted_message}")
    except Exception as e:
        messagebox.showerror("Decryption Error", f"Invalid ciphertext: {e}")

def copy_to_clipboard(output_var):
    text = new_func(output_var)
    if text:
        pyperclip.copy(text)
        messagebox.showinfo("Copied", "Text copied to clipboard!")
    else:
        messagebox.showwarning("Copy Error", "No text to copy!")

def new_func(output_var):
    text = output_var.get()
    return text

def animate_label():
    colors = ["#FF5733", "#33FFBD", "#FF33FF", "#337BFF", "#FFBD33"]
    current_color = animate_label.color_index
    animated_label.config(fg=colors[current_color])
    animate_label.color_index = (current_color + 1) % len(colors)
    root.after(500, animate_label)

animate_label.color_index = 0


p = 61
q = 53
public_key, private_key = generate_keys(p, q)


root = tk.Tk()
root.title("RSA Encryption App")
root.geometry("600x500")
root.config(bg="#F3F3F3")


title_label = tk.Label(
    root, text="RSA Encryption & Decryption", font=("Arial", 20, "bold"), bg="#F3F3F3"
)
title_label.pack(pady=20)


message_label = tk.Label(root, text="Enter your message or ciphertext:", font=("Arial", 14), bg="#F3F3F3")
message_label.pack()

message_entry = tk.Entry(root, font=("Arial", 14), width=40)
message_entry.pack(pady=10)


encrypt_button = tk.Button(root, text="Encrypt", font=("Arial", 14), command=handle_encrypt, bg="#007BFF", fg="black")
encrypt_button.pack(pady=5)


encrypted_output = tk.StringVar()
encrypted_label = tk.Label(root, text="Ciphertext:", font=("Arial", 14), bg="#F3F3F3")
encrypted_label.pack()
encrypted_text = tk.Entry(root, font=("Arial", 14), textvariable=encrypted_output, width=40, state="readonly")
encrypted_text.pack(pady=5)
copy_cipher_button = tk.Button(
    root, text="Copy Ciphertext", font=("Arial", 12), command=lambda: copy_to_clipboard(encrypted_output), bg="#007BFF", fg="black"
)
copy_cipher_button.pack(pady=5)


decrypt_button = tk.Button(root, text="Decrypt", font=("Arial", 14), command=handle_decrypt, bg="#28A745", fg="black")
decrypt_button.pack(pady=10)


decrypted_output = tk.StringVar()
decrypted_label = tk.Label(root, text="Decrypted Message:", font=("Arial", 14), bg="#F3F3F3")
decrypted_label.pack()
decrypted_text = tk.Entry(root, font=("Arial", 14), textvariable=decrypted_output, width=40, state="readonly")
decrypted_text.pack(pady=5)
copy_decrypt_button = tk.Button(
    root, text="Copy Decrypted Message", font=("Arial", 12), command=lambda: copy_to_clipboard(decrypted_output), bg="#28A745", fg="black"
)
copy_decrypt_button.pack(pady=5)


animated_label = tk.Label(root, text="Secure Your Data with RSA!", font=("Arial", 16, "bold"), bg="#F3F3F3")
animated_label.pack(pady=20)
animate_label()


root.mainloop()
