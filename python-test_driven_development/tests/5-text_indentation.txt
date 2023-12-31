# Test Cases for the print_square function

>>> print_square = __import__('4-print_square').print_square

# Test Case 1: Square of size 4
>>> print_square(4)
####
####
####
####

# Test Case 2: Non-integer size
>>> print_square("square")
Traceback (most recent call last):
...
TypeError: size must be an integer

# Test Case 3: Negative size (raises ValueError)
>>> print_square(-1)
Traceback (most recent call last):
...
ValueError: size must be >= 0

# Test Case 4: Square of size 0
>>> print_square(0)


# Test Case 5: Square of size 10
>>> print_square(10)
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########

# Test Case 6: Square of size 1
>>> print_square(1)
#

# Test Case 7: Missing size argument
>>> print_square()
Traceback (most recent call last):
...
TypeError: print_square() missing 1 required positional argument: 'size'
