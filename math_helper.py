# FOR BEST EXPERIENCE, ensure you have gone through 
# 'python_script.py' before consulting this script.

# Let us begin our programming journey by printing
# the the ceremonial phrase to the terminal

print("Hello, World!")

# With that out of the way, let us now print a
# nice introduction to our program

# We could print a big body of text by using
# print("Welcome to...and that is when...lest we forget!...The End.")
# Instead, let us create a variable and define it to contain all
# that we want printed.
intro_text = "Welcome to the greatest math helper you will ever know."

# That is a nice intro, but I think it could use some more text.
intro_text = intro_text + " You may now set aside any of your qualms with math."

# This is another method of adding to variables.
intro_text += " For, joyousness lingers nearer to you now than it ever has!"

# Let us print the varable's text.
print(intro_text)

# Here we will demonstrate how good at math this computer is.

demo_text = "1 + 13/4 - (13 + 4*5)^2 = "

answer = 1 + 13/4 - (13 + 4*5)**2

# Right now our answer is numerical data type (float), but we want a string.
# We can convert it and add it to our demo text like so

demo_text += str(answer)

# Display demo text
print(demo_text)


# This will be the text for the user interface.
# "\n" creates a new line in the text.
interface_text = "Please select what function you want" 
interface_text += " to use by entering its associated number.\n"
interface_text += "1. Adder\n2. Average Finder\n3. Divide with Remainder\n"
interface_text += ">> "


################## FUNCTIONS FOR USE IN THE WHILE LOOP ##################

# A function is a bit of code that can be ran from any point in a program
# after it has been defined.

# This statement does not run any code; it only defines a set of instructions.
# If I want to run the code inside of average_finder, I have to type the
# instruction "average_finder()" in my code.
def average_finder():

	nums = [] # this creates an empty list

	# This will loop until the user inputs "END"
	while True:

		num = input("Enter a number (to stop, enter 'END'): ")

		# "" and '' are interchangeable in Python
		if num == 'END':
			break # this exits the while loop

		num = float(num) # Convert the user's input to a decimal number

		nums.append(num) # add the user's input number to the list

	# Sum up all of the user's inputed numbers and store the result in "total".
	total = 0
	for num in nums:
		total += num

	average = total / len(nums)

	return average

# 'a' and 'b' in this function definition are function arguments.
# Function arguments are values defined when the function is called.
def divide_with_remainder(a, b):

	# a/b might evaluate to some fractional numberm, say 8.63.
	# In this case, int(a /b) = int(8.63) = 8. int(X) will truncate off
	# the part of X which is to the right of the decimal

	# This gets the quotient
	q = int(a / b)

	# "a % b" returns the amount by which 'a' is greater than a
	# multiple of 'b'.

	# This gets the remainder
	r = a % b

	# In Python, a function can return multiple values.
	return q, r
#########################################################################

# A while statement loops all of the code inside of it as long as
# whatever follows it is True. In this case, True will always be
# True so the loop will never end.
# All code inside the while loop must be indented.
while True:

	# This statement will prompt to user with "interface_text"
	# and then allow his (or her) to enter a string.
	# Until the user inputs a string, the program is frozen at this
	# line of code. After the user inputs a string, "user_input"
	# is assigned to reference the value of the user's input string.
	user_input = input(interface_text)


	# An if statement runs the code inside of it iff the statement
	# following "if" evaluates to True. In this instance, if the
	# user inputs a value of "1", then the if statements code will
	# run.
	if user_input == "1":

		iterations = int(input("How many numbers do you want to add?\n>> "))

		total = 0

		for i in range(iterations):

			num = float(input("Enter a number: "))

			total += num

		# Because this print statement is not
		# indented along with "num = ..." and "total += ...",
		# it is not within the if statement
		print("Your total is " + str(total))

	# "elif" means "else if" and will run the code inside iff
	# the previous if statement does not run and the statement
	# directly following "else if" evaluates to True.

	elif user_input == "2":

		average = str(average_finder())

		print("The average is " + average)

	elif user_input == "3":

		a = float(input("Input a dividend (i.e 'a' in a/b): "))
		b = float(input("Input a divisor (i.e 'b' in a/b): "))

		quotient, remainder = divide_with_remainder(a, b)

		print(str(a) + "/" + str(b) + " = " + str(quotient) + " + " + str(remainder))


