"""
your first assignment on conditional statements 
analogy: Microsoft has contracted several companies in nigeria to give jobs to several quolified candidates, and SLNCOnline is in charge of those living with disability because their case is special. But there is a problem.
SLNCOnline do not have the developers to write the code that checks for what microsoft ask them to, and so you are contacted as a python developer that you are. because of some peculiarities, some certain things will be ignored.
For example: the usual age limit is between 18 to 35, but in this case, it's between 18 to 50.
So, your code must meet the following:
collect their user-names and age.
if the persons age is less than 18, tell them to try when their of age.
if the age is within 18 to 50, congradulate them! But also, if the age is within 36 to 50, still congradulate them and add that they are lucky! If not because of their disability, they are already grater than 35 which is greater than the job age limit by Microsoft.
and finally, if the age is greater than 50, tell them they are too old for the job by Microsoft.
"""
# write your name at the end of this line, not below it: Badipe Iseoluwa

# start writing your code below this line: Good luck!

user_name = input("Please enter your :
name here: ")
age = input("\nPlease enter your age here: ")
age = int(age)

if age < 18:
	print("\nSorry you are not old enough. Try again when you are of age!")
elif age <= 35:
	print("\nCongratulations, you qualify for the Job!")
elif age <= 50:
	print("\nCongratulations on getting the job, although you surpass the age limit, due to your disability, you still qualify!")
elif age > 50:
	print("\nSorry, you surpass the age limit for the job by microsoft!")
