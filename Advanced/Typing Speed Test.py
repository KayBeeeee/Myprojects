#The typing speed Test
# We will use Tkinter to build a desktop App
# The App will Assess typing speed
# The Average  speed in 40 words per minute

import tkinter as tk
import time
import random

# Create a window
window = tk.Tk()
window.title("Typing Speed Test")
window.geometry("600x400")

# Create a label
label = tk.Label(window, text="Welcome to the typing speed test")
label.pack()

# Create a text box
text_box = tk.Entry(window)
text_box.pack()

# Create a button
button = tk.Button(window, text="Start")
button.pack()

# Create a label to display the result
result = tk.Label(window, text="")
result.pack()

# Create a function to start the test
def start_test():
    # Get the text from the text box
    text = text_box.get()
    # Split the text into a list of words
    words = text.split()
    # Get the number of words
    num_words = len(words)
    # Get the start time
    start_time = time.time()
    # Get the end time
    end_time = start_time + 60
    # Create a list of random words
    random_words = []
    for i in range(40):
        random_words.append(random.choice(words))
    # Create a label to display the random words
    random_words_label = tk.Label(window, text=" ".join(random_words))
    random_words_label.pack()
    # Create a function to check the result
    def check_result():
        # Get the text from the text box
        text = text_box.get()
        # Split the text into a list of words
        words = text.split()
        # Get the number of words
        num_words = len(words)
        # Get the end time
        end_time = time.time()
        # Get the time taken
        time_taken = end_time - start_time
        # Get the speed
        speed = num_words / time_taken * 60
        # Display the result
        result.config(text="You typed " + str(num_words) + " words in " + str(round(time_taken, 2)) + " seconds. Your speed is " + str(round(speed, 2)) + " words per minute.")
    # Create a button to check the result
    button = tk.Button(window, text="Check Result", command=check_result)
    button.pack()

# Create a button to start the test
button = tk.Button(window, text="Start", command=start_test)
button.pack()

# Start the window
window.mainloop()