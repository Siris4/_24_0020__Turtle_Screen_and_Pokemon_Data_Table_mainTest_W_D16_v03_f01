import prettytable
from _24_0020__OOP_and_Modules_another_module_W_D16_v01 import another_variable, second_variable

print(another_variable)
print(second_variable)

from turtle import Turtle, Screen
tiptup = Turtle()
print(tiptup)
tiptup.shape("turtle")
tiptup.color("orange")
tiptup.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick() #allows the window (screen) to remain open, UNTIL we click on it, and then it exits at that point :)

from prettytable import PrettyTable #prettytable is the Module;  PrettyTable is the Class
table = PrettyTable()  # created an Object (named table), from a PrettyTable Class (notice the Pascal-Type font), and ensure () are at the end. No other . or words needed for this!

table.add_column("Pokemon Name",
["Pikachu","Squirtle", "Charmander"])
table.add_column("Type",
["electric", "water", "fire"])

table.align["Pokemon Name"] = "l"   #NOTE THAT "Pokemon" does not work! You MUST be exactly perfect with the spelling. Like a Dictionary. "Pokemon Name" should be used, in order to work
table.align["Type"] = "l"

print(table.align)

table.align = "l"
print(table.align)

print(table)



