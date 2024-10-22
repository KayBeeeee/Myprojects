#The Password manager App using Tkinter 
# The Password manager App Uses Tkinter to create a simple GUI for storing and retrieving passwords
import tkinter as tk
from tkinter import messagebox

# Dictionary to store passwords
passwords = {}

def add_password():
    """
    Add a new password to the passwords dictionary
    """
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website and username and password:
        passwords[website] = {"username": username, "password": password}
        messagebox.showinfo("Success", "Password added successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please fill in all fields!")

def get_password():
    """
    Retrieve a password from the passwords dictionary
    """
    website = website_entry.get()

    if website in passwords:
        username = passwords[website]["username"]
        password = passwords[website]["password"]
        messagebox.showinfo("Password", f"Username: {username}\nPassword: {password}")
    else:
        messagebox.showerror("Error", "Password not found for this website!")

def clear_entries():
    """
    Clear the entries in the GUI
    """
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Password Manager")

# Create the input fields
website_label = tk.Label(root, text="Website:")
website_label.pack()

website_entry = tk.Entry(root)
website_entry.pack()

username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create the buttons
add_button = tk.Button(root, text="Add Password", command=add_password)
add_button.pack()

get_button = tk.Button(root, text="Get Password", command=get_password)
get_button.pack()

# Start the main event loop
root.mainloop()