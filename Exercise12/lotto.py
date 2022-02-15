# import os

# import the random module
import random
#  the random module is a package from the standard library, it is also a function
#  a module is a file within a python library that has functions within it
# help(random)

# Write a python script called lotto.py that will generate and display 6 unique random lottery numbers between 1 and 50. Use the standard library called random.
# create a variable to hold our random numbers (lottery_number equals an empty set)
#
# for the_numbers in range(6):
#     random_num = random.randrange(1, 51, 1)
#     lottery_number.add(random_num)
#
# print(lottery_number)
#  old code


lottery_number = set(())

# loop over random number generator while the length of the lottery variable is under 6nand add random number to set
while len(lottery_number) < 6:
    random_num = random.randrange(1, 51, 1)
    # adds random number generated to lottery number set
    lottery_number.add(random_num)
print(lottery_number)

# # random = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 50)
# # generates random numbers between 1-50
# random_num = random.randrange(1, 51, 1)
# print(random_num)
# we have used a method on a module
# 1 is the starting point so it can return 1
# we put 51 so it includes all numbers up and including 50
# put at 1 end so the numbers go in 1's
# if put a 3 at the end it would be 1, 4, 7, 10, 13
#  start, stop, step