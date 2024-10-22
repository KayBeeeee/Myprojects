#The converter App Using TKinter
# Importing the necessary modules
import tkinter as tk
from tkinter import ttk

# Creating the main window
root = tk.Tk()
root.title("Converter App")

# Creating the input field
input_field = ttk.Entry(root)
input_field.grid(row=0, column=0, padx=10, pady=10)

# Creating the dropdown menus
input_unit = ttk.Combobox(root, values=["Meter", "Centimeter", "Kilometer"])
input_unit.grid(row=0, column=1, padx=10, pady=10)
input_unit.current(0)

output_unit = ttk.Combobox(root, values=["Meter", "Centimeter", "Kilometer"])
output_unit.grid(row=1, column=1, padx=10, pady=10)
output_unit.current(1)

# Creating the convert button
convert_button = ttk.Button(root, text="Convert")
convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Creating the output field
output_field = ttk.Label(root, text="")
output_field.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Defining the conversion functions
def convert():
    # Get the input value and units
    input_value = float(input_field.get())
    input_unit_value = input_unit.get()
    output_unit_value = output_unit.get()

    # Convert the input value to meters
    if input_unit_value == "Meter":
        meters = input_value
    elif input_unit_value == "Centimeter":
        meters = input_value / 100
    else:
        meters = input_value / 1000

    # Convert the meters to the output unit
    if output_unit_value == "Meter":
        output_value = meters
    elif output_unit_value == "Centimeter":
        output_value = meters * 100
    else:
        output_value = meters * 1000

    # Update the output field
    output_field.config(text=str(output_value))

# Binding the convert function to the button
convert_button.config(command=convert)

# Running the main loop
root.mainloop()