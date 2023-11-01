# using if statement.

weight = input("Give your weight: ")
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    pound_to_kg = 0.45 * float(weight)
    print(f'You are {pound_to_kg} kg')
elif unit.upper() == "K":
    kg_to_pound = 2.20462 * float(weight)
    print(f'You are {kg_to_pound} lbs')
print("Thank you.")
