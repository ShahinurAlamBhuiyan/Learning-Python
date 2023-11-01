numbers = [5, 2, 5, 2, 2]

# using nested
for num in numbers:
    output = ''
    for i in range(0, num):
        output += 'X'
    print(output)

# using concatenation
for num in numbers:
    print("X"*num)



