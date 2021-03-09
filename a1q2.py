# Assignmet - Q2
# Write a Python program to print the numbers in the list which are divisible by 3.

l = list(range(1,20))
div_by_three = []
for i in l:
    if i%3 == 0:
        div_by_three.append(i)
    else:
        continue
print(div_by_three)

