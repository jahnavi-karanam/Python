# 1.Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “Python Training” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string.
x = int(input("Enter a value:"))
if x % 3 == 0:
    if x % 5 == 0:
        print("Consultadd - Python Training")
    else:
        print("Consultadd")
elif x % 5 == 0:
    print("Python Training")

# 2. Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If User Enter 4 - Multiplication
# If User Enter 5 - Average
# Ask user to enter two numbers and keep those numbers in variables num1 and num2
# respectively for the first 4 options mentioned above.
# Ask the user to enter two more numbers as first and second for calculating the average as
# soon as the user chooses an option 5.
# At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”

sel = int(input("Enter your selection:"))
num1 = int(input("Enter value 1:"))
num2 = int(input("Enter value 2:"))

if sel == 1:
    result = num1 + num2
    print("Answer is:", result)
elif sel == 2:
    result = num1 - num2
    print("Answer is:", result)
elif sel == 3:
    result = num1 / num2
    print("Answer is:", result)
elif sel == 4:
    result = num1 * num2
    print("Answer is:", result)
elif sel == 5:
    num3 = int(input("Enter value 3:"))
    num4 = int(input("Enter value 4:"))
    result = (num1 + num2 + num3 + num4) / 4
    print("Average of the numbers is:", result)

if result < 0:
    print("NEGATIVE")
else:
    print("POSITIVE")

# 3. Write a program in Python to implement the given flowchart:

a = 10
b = 20
c = 30
avg = (a + b + c) / 3
print("avg=", avg)
if avg > a and avg > b and avg > c:
    print(avg, "is higher that", a, b, c)
elif avg > a and avg > b:
    print(avg, "is higher than", a, c)
elif avg > a and avg > c:
    print(avg, "is higher than", b, c)
elif avg > a:
    print(avg, "is just higher than", a)
elif avg > b:
    print(avg, "is just higher than", b)
elif avg > c:
    print(avg, "is just higher than", c)

# 4. Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”
game = int(input("Enter a number:"))
if game < 0:
    print("It's Over")
else:
    print("Good going")

# 5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.
li1 = [x for x in range(2000, 3200) if x % 7 == 0 and x % 5 != 0]
print(li1)

# 6. What is the output of the following code examples?
# 1st example question:
# x = 123
# for i in x:
#     print(i)

# 2nd example question:
# i=0
# while i<5:
#     print(i)
#     i+=1
#     if i==3:
#         break
#     else:
#         print("error")
# A: The output will stop as soon as i reaches 3, below is the output
# i is now value 0, 0 is less than 5, but it is not 3, the number along with error is printed.
# i is now value 1, 1 is less than 5,but it is not 3, the number along with error is printed.
# i is now value 2, 2 is less than 5, but it is not 3, the number along with error is printed.
# i is now value 3, 3 is less than 5, but it is 3, so the while loop breaks and it is not printed.
# 0
# error
# 1
# error
# 2
# error

# 3rd example question
# count = 0
# while True:
#     print(count)
#     count+=1
#     if count >= 5:
#         break
# # A. Until the count reaches 5, all the numbers are printed.
# count enters into the while loop with vale 0, 0 gets printed and then it gets incremented by 1.
# The if statement if it's lesser than or equal to 5 it gets into the while loop.' \
# This continues till the count is greater than or equal to 5.
# 0
# 1
# 2
# 3
# 4


# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.

for x in range(6):
    if x == 3 or x == 6:
        continue
        print(x, end='')
        print("\n")

# 8. Write a program that accepts a string as an input from the user and calculate the number of digits and letters.
x = input("Enter a string:")
dig = let = 0
for char in x:
    if char.isdigit():
        dig = dig + 1
    elif char.isalpha():
        let = let + 1
    else:
        pass
    print("No. of Letters:", let)
    print("No. of digits:", dig)

# 9. Read the two parts of the question below:
# Write a program such that it asks users to “guess the lucky number”. If the correct number is
# guessed the program stops, otherwise it continues forever.
luck = int(input("Guess the lucky number:"))
while luck != 6:
    print("Try again!")
    luck = int(input("Guess the lucky number:"))

# Modify the program so that it asks users whether they want to guess again each time. Use two
# variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
# to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
# The program continues as long as a user has not answered “no” and has not guessed the correct
# number)
number = -1
answer = "yes"
while number != 6 and answer != "no":
    number = int(input("Guess the lucky number: "))
    if number != 6:
        print("That is not the lucky number")
        answer = input("Would you like to guess again? ")

# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
# such as
# While counter <= 5:
# print(“Type in the”, counter, “number”
# counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). If the
# correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”.

counter = 1

while counter <= 5:
    number = int(input("Guess the lucky number: "))
    if number != 6 and counter<=5:
        print("Try Again!")
        counter = counter + 1
    else:
        print("Good Guess")

else:
    print("game over!")


#11 In the previous question, insert break after the “Good guess!” print statement. break will terminate
# the while loop so that users do not have to continue guessing after they found the number. If the user
# does not guess the number at all, print “Sorry but that was not very successful”.

counter = 1

while counter <= 5:
    number = int(input("Guess the lucky number: "))
    if number != 6:
        print("Try Again!")
        counter = counter + 1
    else:
        print("Good Guess")
        break
else:
    print("game over!")

