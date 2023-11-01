numbers = [5, 2, 2, 1, 7, 4]

numbers.append(20)  # add 20 in the last position
numbers.insert(0, 10)  # index, object
numbers.remove(5)  # 5 removed
# numbers.clear()  # remove all data
numbers.pop()  # end item remove
numbers.index(7)  # getting index
print(50 in numbers)  # give boolean. False

print(numbers.count(2))  # counting same object

numbers.sort()  # sorting numbers
print(numbers)

numbers.reverse()  # sorting reverse
print(numbers)

numbers2 = numbers.copy()  # copying.
print(numbers2)


