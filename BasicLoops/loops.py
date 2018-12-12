"""
This loop print fizz if a number in given range is a multiple of 3, prints Buzz if the number is a multiple of 5,
print FizzBuzz in a number is a multiple of both 3&5 then print prime if number is prime.
"""


for number in range(1,101):
	if number%3 == 0 and number%5 == 0:
		print("FizzBuzz")
	elif number%3 == 0:
		print("Fizz")
	elif number%5 == 0:
		print("Buzz")
	elif number%2 != 0:
		print("Prime")
		  

