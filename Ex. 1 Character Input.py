'''
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
Extras:

1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''
from datetime import datetime

name = input("Hi! What is your name? ")
age = int(input("Nice to meet you! How old are you? "))
current_date = datetime.now()
current_year = current_date.year
year = current_year + (100 - age)

HB = input("Have you already had your bitrthday this year? ").lower()
if HB == "yes":
    string = "You will be 100 years in " + str(year) + "\n"
    print(string)
elif HB == "no":
    string = "You will be 100 years in " + str((year - 1)) + "\n"
    print(string)
else:
    print("Error")
times = int(input("Tell me random number under 10: "))
i = 0
while times > 10:
    print("Are you sure? It has to be the number less than or equal to 10.")
    n = 1
    i = i + n
    times = int(input("Tell me a random number under 10: "))
    if i == 3:
        print ("I don´t want to play with you!")
        break
