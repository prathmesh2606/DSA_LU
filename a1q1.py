# Assignment 1 - Q1
# Write a python program that takes two numbers as the input such as X and Y and print the result
# of X^Y(X to the power of Y).

# Taking input
x,y = [int(i) for i in input("Enter base value and then power value by giving space between them (eg: 2 3 ans: 8): ").split()]
print(f"{x} to the power of {y} is: {x**y}")
