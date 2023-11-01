# age = int(input('Age: '))  # if input string get ERROR: ValueError
# print(age)

try:
    age = int(input('Age: '))  # if input string get ERROR: ValueError
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age can not be zero')
except ValueError:
    print("Invalid value!")
