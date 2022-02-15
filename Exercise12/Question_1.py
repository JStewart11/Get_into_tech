# what is wrong with the following code?
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'
print(cheese)
# the code above splits the word Oke e.g. O, k, e. The operators =+ appear to split words into letters when adding them.
# QUESTION TO ASK Victoria
# if you want to add a letter, do you use +=?

# correct code (need to add Oke)
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese.append('Oke')
print(cheese)
# the code will add Oke at the end of the list
# The append() method in python adds a SINGLE ITEM to the existing list.

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese[3:4] = ['Oke', 'Mozarella']
print(cheese)
# this adds Oke and Mozarella to the end using the slicing method and indexing.
# use slicing to add more than one item