import tkinter as tk
import random
import string
import threading

def crack_password(p, output_text):
    letters = list(string.ascii_letters) 
    digits = list(string.digits)           
    special_characters = list("`~!@#$%^&*()-_=+[]{}\\|;:'\",<.>/?")

    keyboard_characters = letters + digits + special_characters
    n = len(p)
    count = 0
    
    while True:
        brute = "".join(random.choices(keyboard_characters, k=n))
        output_text.insert(tk.END, brute + "\n")
        output_text.see(tk.END)  # Scroll to the bottom
        count += 1
        if brute == p:
            output_text.insert(tk.END, f"\nPassword is: {brute}\n", "success")
            output_text.insert(tk.END, "Password cracked!\n", "success")
            output_text.insert(tk.END, f"Attempts taken to crack the password: {count}\n", "success")
            break

def start_cracking():
    password = entry.get()
    output_text.delete(1.0, tk.END)  # Clear previous output
    thread = threading.Thread(target=crack_password, args=(password, output_text))
    thread.start()

# Create the main window
root = tk.Tk()
root.title("Password Cracker")
root.geometry("500x600")
root.configure(bg="#2C3E50")

# Create input field
label = tk.Label(root, text="Enter the password:", font=("Arial", 14), bg="#2C3E50", fg="#ECF0F1")
label.pack(pady=10)

entry = tk.Entry(root, show='*', width=30, font=("Arial", 14))
entry.pack(pady=10)

# Create button to start cracking
button = tk.Button(root, text="Crack Password", command=start_cracking, font=("Arial", 14), bg="#27AE60", fg="white")
button.pack(pady=20)

# Create text area to display output
output_text = tk.Text(root, width=50, height=20, font=("Courier New", 12), bg="#34495E", fg="#ECF0F1", insertbackground='white')
output_text.pack(pady=10)

# Add tags for colored output
output_text.tag_config("success", foreground="lightgreen")

# Start the Tkinter main loop
root.mainloop()
