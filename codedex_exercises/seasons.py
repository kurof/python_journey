## --> Seasons
# winter = [1,2,3]
# spring = [4,5,6]
# summer = [7,8,9]
# autumn = [10,11,12]

## --> user input
month = int(input("Agrega un mes de 1 a 12: "))

## --> processing
if month == 1 or month == 2 or month == 3:
    print("Winter 🌨️")
elif month == 4 or month == 5 or month == 6:
    print("Spring 🌱")
elif month == 7 or month == 8 or month == 9:
    print("Summer 🌻")
elif month == 10 or month == 11 or month == 12:
    print("Autumn 🍂")
else:
    print("Invalid")