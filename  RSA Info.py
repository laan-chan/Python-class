import tkinter as tk
from PIL import Image, ImageTk   # type: ignore
import os

rsa_info = {
    "Introduction": (
        "•RSA (Rivest–Shamir–Adleman) is a widely used asymmetric encryption algorithm. "
        "\n•It was introduced in 1977 and remains a cornerstone of modern cryptography."
        "\n•The growing domain of computer networks required a solution to secure digital communication. RSA was initially developed in 1977 as one such solution. The primary focus of RSA was to allow data to be securely transmitted over unsecured networks, specifically to enable private communications over the Internet and other electronic systems."
        "\n•In traditional cryptographic systems, secure key distribution was a challenge. It required both parties to share a secret key before sending or receiving a message. With RSA, public-key cryptography helps users to share their public key openly, while keeping their private key secret. This solved the problem of key distribution and allowed users to communicate securely without prior key sharing."
        "\n•In traditional cryptographic systems, secure key distribution was a challenge. It required both parties to share a secret key before sending or receiving a message. With RSA, public-key cryptography helps users to share their public key openly, while keeping their private key secret. This solved the problem of key distribution and allowed users to communicate securely without prior key sharing."
        "\n•This makes RSA one of the most widely used encryption mechanisms worldwide. However, the computational complexity of RSA, it is not ideal to encrypt a huge amount of data."
        "\n•To manage this goal, RSA is used to encrypt a symmetric key. The key is then used to encrypt the actual huge data. This hybrid approach utilizes both asymmetric and symmetric cryptography for efficient encryption."
    ),
    "How RSA Works": (
        "•RSA uses two keys: a public key for encryption and a private key for decryption. "
        "\n•Its security is based on the mathematical properties of large prime numbers."
        "\n•RSA is based on factorizing and factoring large integers. First, you must choose two large prime numbers for the key pair, which is difficult to factorize. Hence, the prime numbers must be selected randomly and with a substantial difference between them. For example, consider the two chosen prime numbers as p and q."
        "\n•Then, the algorithm calculates their product, denoted by n = p * q. The values of p and q should be kept secret, while n, which is used as the modulus for public and private keys, must be made public."
        "\n•Next, the Carmecheals’ totient function is calculated using p and q, and the integer e, whose value is used as the public exponent, is selected. Then the next step is calculating the value of d, which is used as the private exponent."
    ),
    "Key Generation": (
        "1. Select two large prime numbers (p, q).\n"
        "2. Compute their product: n = p * q.\n"
        "3. Calculate totient: φ(n) = (p-1)(q-1).\n"
        "4. Choose a public key exponent: e (1 < e < φ(n)).\n"
        "5. Compute the private key: d (modular inverse of e mod φ(n))."
    ),
    "Encryption Process": (
        "To encrypt a message M (numerical format), use the public key (e, n):\n"
        "Ciphertext: C = M^e mod n."
    ),
    "Decryption Process": (
        "To decrypt the ciphertext C, use the private key (d, n):\n"
        "Plaintext: M = C^d mod n."
    ),
    "Applications": (
        "1. Secure Communication: Encrypting sensitive data over the internet.\n"
        "2. Digital Signatures: Ensuring authenticity and integrity of messages.\n"
        "3. Key Exchange: Securely exchanging symmetric encryption keys."
        "\n4. Digital certificates"
        
    ),
    "Advantages": (
        "1. Strong security when properly implemented.\n"
        "2. Public key can be shared openly without compromising security.\n"
        "3. Enables digital signatures."
    ),
    "Disadvantages": (
        "1. Computationally expensive, especially for large datasets.\n"
        "2. Vulnerable to attacks if key generation or implementation is flawed.\n"
        "3. Less efficient than symmetric algorithms for large-scale encryption."
        "\n4.Side-channel attacks"
        "\n5.Inadequate key length"
        "\n6.Weaknesses in prime numbers"
        "\n When we talk about prime number weaknesses, we can break it into: Randomness, Closeness"
        "\n7.Lost or stolen keys"
        "\n8.Fault-based attacks"

    ),
}


def show_info(title):
    info_label.config(text=rsa_info[title])

    
    image_path = f"/Users/laanchansreekanta/Documents/python/images/{title.replace(' ', '_').lower()}.png"  

    
    try:
       
        if os.path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((300, 300), Image.Resampling.LANCZOS)  
            photo = ImageTk.PhotoImage(image)

            
            image_label.config(image=photo)
            image_label.image = photo  
        else:
            image_label.config(image='', text="Image not available for this topic.")
    except Exception as e:
        image_label.config(image='', text=f"Error loading image: {e}")


root = tk.Tk()
root.title("Learn About RSA")
root.geometry("800x600")
root.config(bg="#F3F3F3")


title_label = tk.Label(root, text="Learn About RSA Encryption", font=("Arial", 20, "bold"), bg="#F3F3F3")
title_label.pack(pady=10)


button_frame = tk.Frame(root, bg="#F3F3F3")
button_frame.pack(pady=10)

topics = [
    "Introduction",
    "How RSA Works",
    "Key Generation",
    "Encryption Process",
    "Decryption Process",
    "Applications",
    "Advantages",
    "Disadvantages",
]

for topic in topics:
    btn = tk.Button(button_frame, text=topic, font=("Arial", 12), command=lambda t=topic: show_info(t), width=20)
    btn.pack(side=tk.LEFT, padx=5, pady=5)


info_label = tk.Label(root, text="", font=("Arial", 18), bg="#FFFFFF", anchor="nw", justify="left", wraplength=1100, height=20)
info_label.pack(pady=20, fill=tk.BOTH, expand=True)


image_label = tk.Label(root, bg="#F3F3F3", text="Image will be displayed here", font=("Arial", 12, "italic"))
image_label.pack(pady=20)


root.mainloop()
