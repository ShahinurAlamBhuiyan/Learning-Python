# Dictionary is as look as json formate in js.

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])  # John Smith

# print(customer["mobile"])  # keyError!
# print(customer["Name"])  # keyError!


print(customer.get("name"))  # John Smith
print(customer.get("mobile"))  # none

print(customer.get("birthdate", "Sep 19 ,2001"))  # Sep 19 ,2001

customer["name"] = "Shahin Bhuiyan"  # updating name
customer["number"] = "098765456"
print(customer["name"])  # Shahin Bhuiyan
print(customer["number"])  # 098765456
