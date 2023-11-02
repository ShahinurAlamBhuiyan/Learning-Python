class Mammal:
    def walk(self):
        print(f"walking")


# class Dog:
#     def walk(self):
#         print("Walk")

# class Cat():
#     def walk(self):
#         print("Walk")

# instead of this we are using inheritance there for reusing same methods.

class Dog(Mammal):
    def bark(self):  # not use pass, cz it's not empty.
        print(f"bark")


class Cat(Mammal):
    pass  # In py, class can't be empty, that's why used pass.


d1 = Dog()
d1.bark()
d1.walk()



