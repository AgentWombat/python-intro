
# Anything in Python code which follows a '#' will
# be ignored by the interpreter.

# As is the tradition of old, this is how we print
# "Hello, World!" to the command line.
print("Hello, World!")

# We can also store our message (called a "string")
# in a variable
welcome = "Hello, World! (variable)"
print(welcome)

# Python (and computers in general) are good at arithmetic
a = 8**2 - 3 * 2 # = 8^2 - 3x2
print("8^2 - 3x2 =", a)

a = 12
b = 13
c = a + b
print("a, which equals 12, plus b, which equals 13, equals", c)

a = 3
a = a + 3
print("a = 3; a + 3 =", a)

# Shorthand for adding to a variable as follows:
a = 3.5
a += 3
print("a = 3.5; a += 3; results in", a)

# We can also concatonate strings together by 'adding'
a = "This message"
b = " is split across"
c = " multiple variables."
d = a + b + c
print(d)

# To concatonate a number to a string, we must first convert
# the number to a string.
# a = "The number is "
# b = 3
# c = a + b <-- THIS WOULD BE AN EXCEPTION
a = "The number "
b = 3
c = a + str(b) # 'str' stands for 'string'
print(c)

# In a similar since, if we wish to add a string
# to a number in a mathematical sense we have
# to first convert the string to a number.
a = 12
b = '5'
c = a + int(b) # 'int' stands for 'integer'
print('12 + 5 =', c)

a = 12
b = '5.15'
c = a + float(b) # 'float' stands for 'floating point number', which is a fractional value.
print('12 + 5.15 =', c)

# We can get input from a user like so:
user_input = input("What do you want to say? ")
print('No way! I cannot believe you said "' + user_input + '"!')

# 'input' always returns a string value.
# If we want a number from the user, we must convert
# the input using 'int' or 'float'.
user_input = float(input("What is your favorite number? "))
num_plus_gr = user_input + 1.618
print("your number plus 1.618 is " + str(num_plus_gr))

# list can hold a assortments of wonderful informations
print("--LIST--")
a_list = [1, 2, 3, 4, "I", "declare", "a", "thumb", "war"]
print(a_list)
length = len(a_list)
print("The list has", length, "elements." )

# To access information in a list, we must subscript the list using '[]'
# The list indices start at 0 and go up to [length of the list] - 1
print("--INDEXING--")
print(a_list[0])
print(a_list[1])
print(a_list[7])
print(a_list[8])

# Python also supports negative indexing
# Negative indecis start at -1 (last element) and go to -[length of the list]
print(a_list[-9])
print(a_list[-8])
print(a_list[-2])
print(a_list[-1])

# A while-loops repeats code inside itself while a certain condition is met.
# Code is considered inside a while loop if it is indented under the
# while-loop. The below while loop will run as long as variable 'i' is less than
# the length of 'a_list'
print("--WHILE LOOP--")
i = 0
while i < len(a_list):
	element = a_list[i]
	print(i, element)
	i = i + 1

# To access every element in an array, for-loops are quite usefull.
# Everything inside of a for-loop is repeated for each element in
# a list (or other iterable data structure). At each iteration,
# the iterating variable references the next element in the list.
# Code inside a for loop must be indented.
print("--FOR LOOPS--")
for element in a_list:
	print(element)

for McDonalds in a_list:
	print(McDonalds)

print("--FUNCTIONS--")
# Functions are bits of code that can be defined and then called
# later. Functions must be defined before they are called.

def say_hi():

	print("Hi! (from a function)")

print("The functions code does not actually run until we call it.")

# Here we will call the function:
say_hi()
say_hi()
say_hi()

# Function arguments allow functions to be more dynamic

def welcome(name):
	print("Hello, " + name + "!")

welcome("Matthew")
welcome("Mark")
welcome("Luke")

# Functions can also return values.

def square(a):
	return a * a

twelve_squared = square(12)
print("Twelve squared is", twelve_squared)


def find_smallest(a,b,c):

	if a <= b and a <= c:
		return a
	if b <= a and b <= c:
		return b
	if c <= a and c <= b:
		return c 

print("The smallest of 31415, 2.71828, and 1 is", find_smallest(31415, 2.71828, 1))
print("The smallest of 4, 90, and 10 is", find_smallest(4, 90, 10))