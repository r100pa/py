'''
Ben Stephenson, The Python Workbook
My solutions:
'''
# 2
# Hello
name = input("What is your name? ")
print("Hello "+name+"!")

# 3
# Area of a Room
width = float(input("Give me width of the room, in meters: "))
length = float(input("Give me length of the room, in meters: "))
print(F"Area of this room is: {width*length} square meters" )

# 4 
# Area of a Field
width = int(input("Give me width of the field, in feets: "))
length = int(input("Give me length of the field, in feets: "))
print(F"Area of this field is: {(width*length)/43560} acres")

# 5
# Bottle deposits
small = int(input("How many small bottles you will recycle?: "))
large = int(input("How many large bottles you will recycle?: "))
print(F"OK. You will receive ${small * 0.10 + large * 0.25:.2f}")


# 7
# Sum of the first n positive integers
n = int(input("Give me a positive integer: "))
print(f"Sum of numbers from 1 to {n} is: {(n*(n+1))/2}")

# 11
# Fuel efficency
mpg = float(input("Give me fuel efficency in miles per gallon(mpg): "))
print(f"OK. {mpg} mpg will be {378.5411784/(1.609344*mpg):.2f} liters per 100km")

# 13
# Making change

cents = int(input("How many cents to return?: "))

cad200 = cents//200
cad100 = cents%200//100
cad25 = cents%100//25
cad10 = cents%25//10
cad5 = cents%10//5
cad1 = cents%5


print(f"I will return your {cents} cents as: {cad200} x  2CAD, {cad100} x 1CAD, {cad25} x 0.25CAD, {cad10} x 0.10AD, {cad5} x 0.05CAD and {cad1} x 0.01CAD.")
print(f"This will be {cad200+cad100+cad25+cad10+cad5+cad1} coins!")

# 48
# chinese zodiac

# I don't know chinese astrology but if 2000 was year of Dragon and
# 2011 was year of Hare and it is repeated in 12-year cycles I just 
# subtract 2000 and then count modulo

# v1, multiple if's involved as it's chapter 2 called "If Statement Exercises"

year = int(input("Give me a year, please: "))
if (year-2000) % 12 == 0:
    answer = "Dragon"
elif (year-2000) % 12 == 1:
    answer = "Snake"
# .
# .
# .
# and so on
elif (year-2000) % 12 == 10:
    answer = "Tiger"

else:
    answer = "Hare"

print(f"According to chinese zodiac {year} is a year of {answer}")


# v2 shortened, with list

zodiac = ["Dragon", "Snake", "Horse", "Sheep", "Monkey",
          "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Hare"]

year = int(input("Give me a year, please: "))
sign = zodiac[(year - 2000) % 12]

print(f"According to chinese zodiac {year} is a year of {sign}")



# 130
# Text Messaging

