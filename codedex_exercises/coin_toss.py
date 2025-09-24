# importing random library
import random

num = random.randint(0,1) # generating random number 0 -> 1

if num > 0.5:
  print(f"{num} -> Cara")
else:
  print(f"{num} -> Cruz")