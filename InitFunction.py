class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


name_input = input("Name: ")
age_input = input("Age: ")

info = Person(name_input, age_input)

print("Your Name: " + info.name)
print("Your Age:  " + info.age)
