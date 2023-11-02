class Point:
    def __init__(self, x, y):
        print("constructor.")
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


# point1 = Point()
# point1.draw()
# point1.x = 20
# point1.y = 10
# print(point1.x)
#
# point2 = Point()
# point2.x = 1
# print(point2.x)

point = Point(10, 20)
print(point.x)
