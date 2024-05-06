#!/usr/bin/python3
import sys

# Function Description: This function calculates the factorial of a given integer.
# Parameters:
#   - n: Integer for which we want to calculate the factorial.
# Returns:
#   - The value of the factorial of n.
def factorial(n):
    # If n is equal to zero, the factorial is 1.
    if n == 0:
        return 1
    # Otherwise, we calculate the factorial recursively by multiplying n by the factorial of n-1.
    else:
        return n * factorial(n-1)

# Calling the factorial function with the argument passed in the command line.
f = factorial(int(sys.argv[1]))
print(f)
