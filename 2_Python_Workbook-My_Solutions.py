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

# 35
# Dog years
dogyears = int(input("How old is this dog? "))

if dogyears < 0 : 
    print("Sorry, but age cannot be negative!")
    dogyears = int(input("How old is this dog? "))

if dogyears < 2 :
    humanyears = dogyears * 10.5
else:
    humanyears = 21 + (dogyears - 2) * 4

print(f"Dog that is {dogyears} years old is {humanyears} human years old.")

# 37
# Name that shape

sides = int(input("How many sides?: "))
if sides < 3 or sides > 10: polygon ="error"
elif sides == 3: polygon = "triangle"
elif sides == 4: polygon = "rectangle"
elif sides == 5: polygon = "pentagon"
elif sides == 6: polygon = "hexagon"
elif sides == 7: polygon = "heptagon"
elif sides == 8: polygon = "octagon"            
elif sides == 9: polygon = "nonagon"
else: polygon = "decagon"

if polygon == "error": print("Sorry, I don't know name of such shape")
else: print(f"If shape has {sides} sides then it is called {polygon}.")

# 45
# What Color is that Square?

field = input("Enter a square position (like a1 or b5): ")
row = int(field[-1])

if row % 2 != 0 : start = "black"
else: start = "white"

if start == "black":
    if field[0] == "a" or field[0] == "c" or field[0] =="e" or field[0] == "g": color = "black"
    else: color = "white"

if start == "white":
    if field[0] == "b" or field[0] == "d" or field[0] =="f" or field[0] == "h": color = "black"
    else: color = "white"

print(f"Square {field} is {color}")


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

# 56
# Cell Phone Bill

plan = 15
minutes_included = 50
sms_included = 50
minute_cost = 0.25
sms_cost = 0.15
charge911 = 0.44
tax = 0.05

minutes = int(input("How many minutes did you use this month?: "))
sms = int(input("How many smses did you use this month?: "))

extra_minutes = 0
extra_sms = 0

print (f"Base charge: {plan:.2f}$")
if minutes > minutes_included:
    extra_minutes = (minutes - minutes_included) * minute_cost 
    print(f"Additional minutes charge: {extra_minutes:.2f}$")
if sms > sms_included:
    extra_sms = (sms - sms_included) * sms_cost
    print(f"Additional sms charge: {extra_sms:.2f}$")
print (f"911 line charge: {charge911}$")
print (f"Tax: {(plan+extra_minutes+extra_sms+charge911)*tax:.2f}$")
print (f"Total: {plan+extra_minutes+extra_sms+charge911+tax:.2f}$")


## 57
## Is it a Leap Year?

year = int(input("Enter year: "))

if year % 400 == 0:
    leap = True
elif year % 100 == 0:
    leap = False
elif year % 4 == 0:
    leap = True
else:
    leap = False

if leap:
    print("Year", year, "is leap.")
else:
    print("Year", year, "is not leap.")



# 61
# Average


counter = 0
sum_i = 0

i = None

while i != 0:
    i = int(input("Enter the number: "))
    sum_i += i
    counter += 1
    
if counter == 1:
    print("You have not entered any valid number. Average will not be calculated")
else:
    print(f"Average of numbers you've just entered is: {sum_i / (counter-1)}")

# 69
# Approximate Pi


start = 2
pi = 3

for i in range(1,16):
    if i % 2 == 1:
        pi_addition = 4 / (start * (start + 1) * (start + 2))
        pi_substraction = 0
        start = start + 2
        pi =  pi + pi_addition - pi_substraction
        print(pi)

    else:
        pi_addition = 0
        pi_substraction = 4 / (start * (start + 1) * (start + 2))
        start = start + 2
        pi =  pi + pi_addition - pi_substraction
        print(pi)

# 71
# Square root

x = int(input("Enter number: "))

guess = x / 2

while abs(guess*guess - x) >= 10**-12:
    guess = (guess + x / guess) / 2

print(guess)

# 74
# Multiplication table

print("    ",end="")
for i in range (1,11):
    print('{:4d}'.format(i), end="")
print("\n")

for i in range (1,11):
    print('{:4d}'.format(i), end="")
    for j in range(1,11):
        print ('{:4d}'.format(i * j),end="")
    print("\n")



# 75
# Greatest common divisor

n = int(input("Enter first number: "))
m = int(input("Enter second number: "))

d = min(n,m)

while (m % d != 0) or (n % d != 0):
    d = d - 1

print(d)

# 76
# Prime Factors
n = int(input("Enter integer greater than 1: "))
if n < 2:
    print("I said 'GREATER THAN 1!'")
factor = 2
print("The prime factors of",n,"are:")
while factor <= n:
    if n % factor == 0:
        print(factor)
        n = n//factor
    else:
        factor = factor + 1

# 77
# Binary to Decimal

b = input("Enter binary number: ")
#‭11101011‬
b = b[::-1]
#11010111

d = 0
for pos in range(len(b)):
    d = d + int(b[pos]) * 2 ** pos

print(d)        


# 104
# Sorted Order

l = []
i = None

while i != 0:
    i = int(input("Enter the number: "))
    if i !=0 : l.append(i)


for num in sorted(l):
    print(num)

# 105
# Reverse Order

l = []
i = None

while i != 0:
    i = int(input("Enter the number: "))
    if i !=0 : l.append(i)

#v1
# for num in sorted(l, reverse=True):
#v2
for num in reversed(sorted(l)):
    print(num)


# 109
# List of proper divisors

def properDivisors(n):
    result = []
    for val in range (1,n):
        if n % val == 0:
            result.append(val)
    return result

def main():
    n = int(input("Enter any number: "))
    print("Proper divisors of",n,"are:",properDivisors(n))

if __name__ == '__main__':
    main()

# 121
# Count the Elements

def countRange(l,mi,ma):
    result = 0
    for val in l:
        if val >= mi and val < ma:
            result = result + 1
    return result


def main():
    l1 = [0,1,2,3,4,5,6,7,8,9]
    l2 = [0.1,0.2,0.3,0.4,0.5]
    print(countRange(l1,2,8))
    print(countRange(l1,0,10))
    print(countRange(l2,0.11,0.19))
    print(countRange(l2,0.11,0.49))

main()

# 127
# The Sieve of Eratosthenes

limit = int(input("Enter limit for the sieve: "))
table = [x for x in range(2,limit+1)]

for val in range(2,limit+1):
    factor = 2
    while val * factor <= limit:
        if (val*factor) in table:
            table.remove(val*factor)
        factor = factor + 1

print(table)

# 130
# Text Messaging

# 164
# Total the Values

def add():
    number = input("Enter number: ")
    if number != "":
       global total
       total  = total + float(number)
       add()
    return total

def main():
    global total
    total = 0
    add()
    print(total)

main()