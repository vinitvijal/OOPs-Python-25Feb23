class Person:
    count = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

        Person.count += 1

# Path: main.py

p1 = Person("John", 36, 100000)
print(p1.count)
p2 = Person("Marie", 25, 80000)
print(p2.count)
p3 = Person("Alan", 30, 90000)
print(p3.count)

