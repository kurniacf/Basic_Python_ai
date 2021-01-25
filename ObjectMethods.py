class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("Hello My Name is " + self.name)
        print("My Age is " + self.age)


name_input = input("Name: ")
age_input = input("Age: ")

info = Person(name_input, age_input)
info.myFunc()
