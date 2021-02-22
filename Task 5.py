#1. Write a program in Python to allow the error of syntax to be handled using exception handling.
# HINT: Use SyntaxError
## Need some clarity in this
try:
    eval('x===x')
except SyntaxError:
    print( "you cannot do that")


#2. Write a program in Python to allow the user to open a file by using the argv module. If the
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure
# to use read only mode.

## Need some help with this question.

#3. Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits”
try:
    pin = int(input("Please enter your pin: "))
    for i in pin:
        if len(pin) > 4:
          print("The length is too short/long !!! Please provide only four digits")
except:
    print("Welcome! You entered a valid pin")

#4. Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
# should not be more than 3 times.

count = 0
while True:
    userName = input("Hello! Welcome !! \n\nUsername: ")
    password = input("Password: ")
    count += 1
    if count == 3:
        print("You have entered too many times!")
        break
    else:
        if userName == 'elmo' and password == 'blue':
            print("You are in!")
            break
        else:
            print("Please try again")

#5. Go through the link provided below to understand finally and raise concept:
##Went though the link.


#6. Read doc.txt file using Python File handling concept and return only the even length string from
# the file. Consider the content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string
# Which is of even length
# Make sure you return the content in The same link as it is present.

with open("doc.txt") as f:
    # f.write("Hello I am a file\nWhere you need to return the data string\nWhich is of even length\nMake sure you return the content in The same link as it is present.")
  for line in f:
        if len(line)%2==0:
            print(line)
f.close()