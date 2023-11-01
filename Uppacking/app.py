coordinates = (1, 2, 3)  # (x, y, z)


# without unpacking.
a = coordinates[0]
b = coordinates[1]
c = coordinates[2]

# unpacking the tuples into 3 variables
x, y, z = coordinates  # are the same as a, b, c in top

print(x)  # 1
print(y)  # 2
print(z)  # 3

# we can use this also in list.
coordinates2 = [5, 6, 7]
k, m, n = coordinates2

print(k)  # 5
print(m)  # 6
print(n)  # 7





