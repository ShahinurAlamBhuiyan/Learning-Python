# Find the largest number in a list.

numbers = [4, 1, 11, 11, 9, 4, 2, 2, 3, 3, 9]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Max : {max_num}")


# Remove the duplicates in a list.
for num in numbers:
    if numbers.count(num) > 1:
        numbers.remove(num)
print(numbers)

# another way
uniques = []
for num in numbers:
    if num not in uniques:
        uniques.append(num)
print(uniques)
