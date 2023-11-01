for item in 'Python':
    print(item)


for item in ['Shahin', 'Tonmay', 'Amit']:
    print(item)

for item in range(5, 10):  # 5 include, 10 is excluded
    print(item)


prices = [10, 20, 40]  # show the sum
total = 0
for price in prices:
    total += price
print(f'Total price: {total}')
