matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[1][1] = 20
print(matrix[0])  # [1, 2, 3]
print(matrix[0][2])  # 3
print(matrix[1][1])  # 20

# printing all item.
for row in matrix:
    for item in row:
        print(item)

