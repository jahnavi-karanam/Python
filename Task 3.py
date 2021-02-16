# 1. Create a list of 10 elements of four different data types like int, string, complex and float.
# a = [2,5,1,5,87,34,25,88,33,3]
# b= ['a','b','c','d','e','f','g','h','i','j']
# c=[(3+4i),(4+1i),(6+9i),(8+8i),(9+0i),(3+6i),(5+5i),(2+2i),(1+7i),(5+6i)]
# d=[5.1,3.2,4.3,6.7,8.0,0.2,0.4,8.1,8.9,1.0]

# 2.Create a list of size 5 and execute the slicing structure

a = [3, 6, 2, 7, 1]
print(a[1:4])

# 3.Write a program to get the sum and multiply of all the items in a given list.

y = [1, 2, -8]


def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers


def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot


print(sum_list(y))
print(multiply_list(y))

# 4.Find the largest and smallest number from a given list.

li = [1, 5, 26, 6, 5, 0, 6, 8]


def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max


print(max_num_in_list(li))


def smallest_num_in_list(list):
    min = list[0]
    for a in list:
        if a < min:
            min = a
    return min


print(smallest_num_in_list(li))

# 5. Create a new list which contains the specified numbers after removing the even numbers from a
# predefined list.

list = [10, 1, 3, 5, 7, 22, 33, 50, 44, 55]

print("Original list:")
print(list)

for i in list:
    if (i % 2 == 0):
        list.remove(i)

print("list after removing EVEN numbers:")
print(list)


# 6. Create a list of elements such that it contains the squares of the first and last 5 elements between
# 1 and30 (both included).

## why am i not getting 30 when i put range as 30 ?

def printValues():
    l = list()
    for i in range(1, 31):
        l.append(i ** 2)
    print(l[0:5], l[-5:])


printValues()

# 7. Write a program to replace the last element in a list with another list.
# Sample input: [1,3,5,7,9,10], [2,4,6,8]
# Expected output: [1,3,5,7,9,2,4,6,8]

l1 = [1, 3, 5, 7, 9, 10]
l2 = [2, 4, 6, 8]
l1.extend(l2)
print(l1)

# #8. Create a new dictionary by concatenating the following two dictionaries:
# Sample input: a={1:10,2:20} b={3:30,4:40}
# Expected output: {1:10,2:20,3:30,4:40}

a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
a.update(b)
print(a)

# 9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
# and n(both 1 and n included).
# Sample input: n=5
# Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}

n = int(input("Enter your max value:"))
myDict = {}
for x in range(1, n + 1):
    myDict[x] = x * x
print(myDict)

# 10. Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string.
# Sample input: 34,67,55,33,12,98
# Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)

values = input("Input some comma separated numbers : ")
l2 = values.split(",")
l3 = tuple(l2)
print("list values:", l2)
print("Tuple values:", l3)
