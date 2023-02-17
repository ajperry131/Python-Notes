# bad example of multiple inheritance
class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):  # manager inherits the first version of the method found in Emplyoee
    pass


# good example of multiple inheritance
class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass


# another good example of multiple inheritance
class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")
