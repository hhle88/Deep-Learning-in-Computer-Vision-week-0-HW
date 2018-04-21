# week 0 - hw 2.4 - PyCharm
# Problem:
# Write a Python program to test whether a number is within 100 of 1000 or 2000


# Solution
print('Please insert a number:')
number = int(input())
if 1100 >= number >= 900:
    print('True! This number is within 100 of 1000 or 2000')
elif 2100 >= number >= 1900:
    print('this number is within 100 of 2000')
else:
    print('False! This number is not within 100 of either 1000 or 2000')
