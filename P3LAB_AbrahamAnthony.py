 # Your Name: Antony Abraham
 # Date: 27 JUNE 2026
 # Assignment Name: P3LAB
 # A brief description of the project: This program allows the user to enter a money (float) value with two places after the decimal and the calculates the most efficient 
 # number of dollars, quarters, dimes, nickels, and pennies needed to make the given amount of money.

#Instructions:

#-Make sure you have thoroughly explored the files for this Module from our course e-book.
#-For this assignment, write a Python program as described below.
#-Ensure you have a comment block at the top of your file as we have in previous assignments.
#-After confirming the code produces the required results, save it as P3LAB_LastnameFirstname. Make sure you replace Lastname and Firstname with your actual last and first names.
#-Submit your finished code through the P3LAB assignment link by the posted deadline along with a screenshot of your program's output. Ensure your name is part of the filename and visible in the screenshot.


#Get an amount of money from the user and limit entry to two places after the decimal.
amount = float(input("Enter the amount of money as a float: $"))

#convert the float to an integer and use floor division to generate whole numbers for the counts 
change = round(amount * 100)

# Declare variables
dollars = 100
quarters = 25
dimes = 10
nickles = 5
pennies = 1

# determine number of dollars needed
numDollars = change // dollars 
change = change - (numDollars * dollars)

# determine number of quarters needed
numQuarters = change // quarters 
change = change - (numQuarters * quarters)

# determine number of dimes needed
numDimes = change // dimes 
change = change - (numDimes * dimes)

# determine number of nickles needed
numNickles = change // nickles 
change = change - (numNickles * nickles)

# determine number of pennies needed
numPennies = change // pennies 
change = change - (numPennies * pennies)

# Conditional statements to determine number of coins in each category

if change == 0:
    print("No change")

if numDollars > 0:
    if numDollars == 1:
        print(f"{numDollars} Dollar")
    else:
        print(f"{numDollars} Dollars")

if numQuarters > 0:
    if numQuarters == 1:
        print(f"{numQuarters} Quarter")
    else:
        print(f"{numQuarters} Quarters")

if numDimes > 0:
    if numDimes == 1:
        print(f"{numDimes} Dime")
    else:
        print(f"{numDimes} Dimes")

if numNickles > 0:
    if numNickles == 1:
        print(f"{numNickles} Nickle")
    else:
        print(f"{numNickles} Nickles")

if numPennies > 0:
    if numPennies == 1:
        print(f"{numPennies} Penny")
    else:
        print(f"{numPennies} Pennies")

