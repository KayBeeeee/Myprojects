#prettytable is a python library that allows us to create tables in the terminal
from prettytable import PrettyTable

#creating a table object
table = PrettyTable()

#adding columns to the table
table.field_names = ["Pokemon Name", "Type"]

#adding rows to the table
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

#displaying the table
print(table)