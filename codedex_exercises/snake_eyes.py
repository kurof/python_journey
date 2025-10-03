# importing random library
import random

total = 0 # to store the sum of both dices

# loop
while total != 2:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    print("Nope")
else:
    print("Snake Eyes!")

## --> Otro ejercicio
for i in range(1,24):
    print("* " * i)

## --> otro reto
print("\n")

# Write code below 💖
# variables
# number = int(input("Write a number: "))
# total = 0

# # loop 
# for i in range(1, number+1): # to reach the intended number
#   prod = i*i
#   total += prod
#   print(prod, total)

# print(total)

## --> Otro challenge
# variable
awty_input = ""
# loop
while awty_input != "Yes":
  awty_input = input("Are we there yet? ")

  if awty_input == "Yes":
    print("Yay!")
    break