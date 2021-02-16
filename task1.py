#1. Create three variables in a single line and assign values to them in such a manner that each one of them belongs to a different data type.

x = 4
y = 234.345
z = "Test_string"
print("The variables are:", x, y, z)

#2. Create a variable of type complex and swap it with another variable of type integer.
x = 7+9j
y = 34
temp = x
x = y
y = temp
print("New value for x is:", x)

#3. Swap two numbers using a third variable and do the same task without using any third variable.
 ##Swapping with a third variable
x = 45
y = 65
temp = x
x = y
y = temp
print("Vale of x:", x)
print ("Value of y:", y)

##Swapping without using 3rd variable
x = 45
y = 70
print("Before swapping:")
print("Value of x:",x,"and y:",y)

x , y = y , x
print("After swapping:")
print("Value of x:", x ,"and y", y)

#4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.Version.
##Python 3.x
x = input("Enter a value:")
print(x)

##Python 2.x
## Answer --> x = raw_input("Enter a value:")

#5. Write a program to complete the task given below:
#Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in another variable called z. Add 30 to z and store the output in variable result and print result as the final output.
x = 5
y = 9
z = x+y
t = z+30
print("The sum is:", t)

#6. Write a program to check the data type of the entered values.
x = eval(input("Enter a value:"))
print(type(x))

#7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.
x = "ThisIsAnExampleOfUpperCamelCase"
print(x)
y = "thisIsAnExampleOfLowerCamelCase"
print(y)
z = "this_is_an_example_of_snake_case"
print(z)
w = "THIS IS AN EXAMPLE OF UPPERCASE"
print(w)

#8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
# again. Will it change the value? If Yes then Why?
# answer: Yes, the assigned value 'a' will be changed.
# Variables are like an empty box. Any data type can be assigned to it.
# One you re-assign a data type, the old value gets emptied out and new value is stored.

