print("I will now count my chickens:")

# Hens:  first operation is 30 / 6 = 5; second is 25 + 5 = 30
print("Hens", 25 + 30 / 6)
# Roosters:  first operation is 25 * 3 = 75; second is getting the remainder
# of 75 / 4 = 3 (4 goes into 75 18 times with a remainder of 3)
print("Roosters", 100 - 25 * 3 % 4)
roosters = (100 - 25 * 3 % 4)
print(float(roosters))
print(type(100 - 25 * 3 % 4))
print((100 - 25 * 3 % 4))

print("Now I will count the eggs:")
# First operation is 4 % 2 = 0; next is 1/4 = 0.25
# Adding & subtracting are the last operations:  1 + 0 - 0.25 + 6 = 6.75
print( 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more?")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
