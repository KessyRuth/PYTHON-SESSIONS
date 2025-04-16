# Base class: Person
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def introduce(self):
        print(f"Hi, I'm {self.name}, I'm {self.age} years old and I work as a {self.occupation}.")

    def work(self):
        print(f"{self.name} is working as a {self.occupation}.")

# Subclass: Student (inherits from Person)
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age, "Student")
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}.")

    # Polymorphic method (overrides work)
    def work(self):
        print(f"{self.name} is doing assignments and attending classes.")

# Creating objects
p1 = Person("Alex", 30, "Engineer")
s1 = Student("Lina", 22, "Software Engineering")

p1.introduce()
p1.work()

print()

s1.introduce()
s1.study()
s1.work()

class Person:
    def move(self):
        pass

class Athlete(Person):
    def move(self):
        print("Runs on the track.")

class Dancer(Person):
    def move(self):
        print("Moves rhythmically to music.")

class Driver(Person):
    def move(self):
        print("Drives a vehicle carefully.")

# Polymorphism in action
people = [Athlete(), Dancer(), Driver()]

for person in people:
    person.move()
