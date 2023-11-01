# Tuples are similar to list, so can use them to store.
# But we can't modify them. Tuples are immutable.

numbers = [1, 2, 3]  # it's a list
tuple_numbers = (1, 2, 3)  # it's a tuples

# these are the two methods of tuples
print(tuple_numbers.count(2))
print(tuple_numbers.index(1))

# tuple_numbers[0] = 10  # getting error.

