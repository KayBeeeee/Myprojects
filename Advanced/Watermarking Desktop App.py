#Watermark Desktop App using Python
# We will upload images and add a watermark
# We will use Pillow library for this
# We will use Tkinter for the GUI
# We will use PyInstaller to convert the app to an executable

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Create the main window
root = Tk()
root.title("Watermark Desktop App")
root.geometry("500x500")

# Create a canvas to display the image
canvas = Canvas(root, width=500, height=500)
canvas.pack()

# Create a label to display the image
label = Label(root, text="Select an image to watermark")
label.pack()

# Create a button to select an image
def select_image():
    """
    Open a file dialog to select an image file.
    Load the image and display it on the canvas.
    """
    global img
    img_path = filedialog.askopenfilename()
    img = Image.open(img_path)
    img = img.resize((500, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=NW, image=img)

# Create a button to add a watermark
def add_watermark():
    """
    Add a watermark to the selected image.
    The watermark text is "Watermark".
    The font size is 50.
    The font color is white.
    The watermark is positioned in the bottom right corner of the image.
    """
    global img
    img = img.resize((500, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=NW, image=img)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 50)
    draw.text((250, 250), "Watermark", font=font, fill=(255, 255, 255))
    canvas.create_image(0, 0, anchor=NW, image=img)

# Create a button to select an image
select_button = Button(root, text="Select an image", command=select_image)
select_button.pack()

# Create a button to add a watermark
watermark_button = Button(root, text="Add a watermark", command=add_watermark)
watermark_button.pack()

root.mainloop()
