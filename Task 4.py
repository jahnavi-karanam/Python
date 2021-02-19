# 1. Write a program to reverse a string.
# Sample input: “1234abcd”
# Expected output: “dcba4321”

reverse=input("Enter your string:")
length=len(reverse)
result=reverse[length::-1]
print(result)

#2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12
def Count(up_low):
    upper, lower = 0, 0
    for i in range(len(up_low)):
        if up_low[i].isupper():
            upper += 1
        elif up_low[i].islower():
            lower += 1

    print('Upper case letters:', upper)
    print('Lower case letters:', lower)

up_low = input("Enter your string:")
Count(up_low)

#3. Create a function that takes a list and returns a new list with unique elements of the first list.

def unique(list1):
    list_set=set(list1)
    unique_list1=[list(list_set)]
    for x in unique_list1:
        print(x)
list1=[1,3,5,65,32,1,1,2,88,32,65]
print("List 1 values: ",list1)
print("Unique values from 1st list is: ")
unique(list1)

#4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.

print("Enter your string: ")
lst=[n for n in input().split('-')]
lst.sort()
print("Sorted:")
print('-'.join(lst))

#5. Write a program that accepts a sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT

l=input("Enter your string:")
print("Your string in all caps is: ",l.upper())

#6. Define a function that can receive two integral numbers in string form and compute their sum and
# print it in the console.

x=input("Enter your first string: ")
y=input("Enter your second string: ")
sum=lambda x,y:int(x)+int(y)
print(sum(x,y))

## another way for the question
x=input("Enter your first string: ")
y=input("Enter your second string: ")
def sum(x,y):
    return int(x)+int(y)
print(sum(x,y))

#7. Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line
# by line.

l1=input("Enter your first string value: ")
l2=input("Enter your second string value: ")
if len(l1)>len(l2):
    print(l1)
elif len(l2)>len(l1):
    print(l2)
elif len(l1) == len(l2):
    print(l1)
    print(l2)

#8. Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).

def printTuple():
    lst=(i**2 for i in range(1,21))
    print(tuple(lst))
printTuple()

#9. Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3) (where limit=3)
# Expected output:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

n = int(input("Enter the limit: "))
i = 0
while i < n + 1:
    print(str(i) + " EVEN" if i % 2 == 0 else str(i) + " ODD" )
    i += 1

## Another way for this

limit = int(input("Enter the limit: "))
def showNumbers(limit):
    for i in range(0, limit + 1):
        if i % 2 == 0:
            print(i, end="")
            print(" EVEN")
        else:
            print(i, end="")
            print(" ODD")


showNumbers(limit)

#10. Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)

x=filter(lambda x:x%2==0, range(1,21))
print(list(x))

#11. Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
# numbers in the filtered list. Use lambda() to define anonymous functions.

x=map(lambda x:x**2,filter(lambda x:x%2==0, range(1,11)))
print(x)

#12. Write a function to compute 5/0 and use try/except to catch the exceptions
def divide():
    return 5/0
try:
    divide()
except ZeroDivisionError as z:
    print("Cannot divide by zero")
except:
    print("Can be divisible")


#13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
from functools import reduce
s = reduce(lambda s, x: s + str(x), [1, 2, 3, 4, 5, 6, 7], '')
print(s)


#14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.

n=int(input("Enter your range: "))
integers = range(n)
odd= filter(lambda integers: integers%7==0 and integers%3!=0,integers )
print(list(odd))


#15. Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.
def mul(x):
    return x*x
y=[2,4,5,6,7]
x=map(mul,y)
print(list(x))

#16. What is the output of the following codes:
# (i) def foo():
# try:
# return 1
# finally:
# return 2
# k = foo()
# print(k)

# Output is -- 2

# (ii) def a():
# try:
# f(x, 4)
# finally:
# print('after f')
# print('after f?')
# a()

# Output is -- after f
#              after f?
