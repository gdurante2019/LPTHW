# ex5a.py
# Modify variable names to remove "my_".  Remeber to do this in print statements as well.

name = 'Zed A. Shaw'
age = 35 # not a lie (hmmm...)
height = 74 # inches
weight = 180 # pounds
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually, that's not too heavy.")
print(f"He's got {eyes} and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky; try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, I get {total}.")