from collections import namedtuple


# class Point:  # this is a basic data class, it has only data and no methods
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


Point = namedtuple("Point", ["x", "y"])  # namedtuple can be a faster way to create basic data classes
p1 = Point(x=1, y=2)
# p1.x = 10  # namedtuples are immutable, this will not work
p2 = Point(x=1, y=2)
print(p1 == p2)
