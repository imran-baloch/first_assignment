# -*- coding: utf-8 -*-
"""first_assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14gnsx9JyRMvLnY1XlHscFL8EoKUXgZzy
"""



"""Part 1: Temperature Comparison
Problem Statement:
Write a program that:
● Takes input for the temperatures of two cities in Celsius.
● Compares the temperatures using relational operators (>, <, ==, !=).
Prints a message like:
City A is hotter than City B.
"""

city1_temp = input("Enter city temperature in Celsius")
city2_temp = input("Enter city temperature in Celsius")
if city1_temp > city2_temp:
    print("City A is hotter than City B")
elif city1_temp < city2_temp:
    print("City B is hotter than City A")



"""Part 2: Bill Splitter
Problem Statement:
Write a program that calculates how much each person needs to pay when splitting a bill:
1. Take the total bill amount as input.
2. Take the number of people as input.
3. Calculate each person’s share by dividing the total amount by the number of people.
Print the result in this format:
Total Bill: $[amount]
Number of People: [people]
Each Person Pays: $[share]
"""

total_bill_amount = input("Enter total bill amount : ")
number_of_people = input("Enter number of people : ")
each_person_pays = float(total_bill_amount) / float(number_of_people)
print("Total Bill is Rs." + total_bill_amount)
print("Number of People is " + number_of_people)
print("Each Person Pays Rs. " + str(each_person_pays))



"""Part 3: Custom Message Formatter
Problem Statement:
Write a program that takes the following inputs:
● A name
● A favorite color
● A favorite number
Use string formatting to display the result:

[Name] loves the color [Color] and their favorite number is
[Number].
"""

name = input("Enter your name : ")
favorite_color = input("Enter your favorite color : ")
favorite_number = input("Enter your favorite number : ")
print(name + " loves the color " + favorite_color + " and their favorite number is " + favorite_number)



"""Part 4: Two-Number Relationship
Problem Statement:
Write a program that:
1. Takes two numbers as input.
2. Checks and displays their relationship using these conditions:
○ Whether the first number is greater than, less than, or equal to the second
number.
○ Whether both numbers are even or odd.

Print the results in this format:
Number 1: [num1]
Number 2: [num2]
Relationship: [Greater than/Less than/Equal]
Both numbers are [Even/Odd/Mixed].
"""

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
  print(f"{num1} and {num2} are equal.")

"""Part 5: Rectangle Calculator
Problem Statement:
Write a program that calculates and displays the area and perimeter of a rectangle:
1. Take the length and width of the rectangle as inputs.
2. Calculate the area and perimeter using basic arithmetic operators.
Print the result in this format:
Length: [length]
Width: [width]
Area: [area]
Perimeter: [perimeter]
"""

length = int(input("Enter the length of the room in feet: "))
width = int(input("Enter the width of the room in feet: "))
rectangel = length * width
perimdeter = 2 * (length + width)
print("The rectangel is "+ str(rectangel))
print("Perimeter is "+ str(perimdeter))



"""Part 6: Age Difference Calculator
Problem Statement:
Write a program that:
1. Takes the ages of two people as input.

2. Calculates the difference in their ages using subtraction.
Prints the result using string formatting:
The age difference between [Person1] and [Person2] is: [Difference]
years.
"""

person1 = int(input("Enter the first person age : "))
person2 = int(input("Enter the second person age : "))
age_difference = (person1 - person2)
print(f"The age differnce between {person1} and {person2} is {age_difference} years")



"""Part 7: Days to Seconds Converter
Problem Statement:
Write a program that:
1. Takes the number of days as input.
2. Converts the input into seconds using this formula:
Seconds=Days×24×60×60
Prints the result using string formatting:
[Days] days are equal to [Seconds] seconds.
"""

days = int(input("Enter the days in numbers : "))
seconds = days * 24 * 60 * 60
print(f"{days} days are equal to {seconds}")



"""Part 8: Arithmetic Checker
Problem Statement:
Write a program that:
1. Takes two numbers as input.
2. Prompts the user to input an arithmetic operator (+, -, *, /).
Performs the operation on the numbers and prints the result.
[Number1] [Operator] [Number2] = [Result]
"""

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operator = input("Enter your operators (+, -, *, /)")

if operator == "+":
    result = number1 + number2
    print(f"{number1} + {number2} equals to {result}")
elif operator == "-":
    result = number1 - number2
    print(f"{number1} - {number2} equals to {result}")
elif operator == "/":
    result = number1 / number2
    print(f"{number1} / {number2} equals to {result}")
elif operator == "*":
    result = number1 * number2
    print(f"{number1} x {number2} equals to {result}")

2