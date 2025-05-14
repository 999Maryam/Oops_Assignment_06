# step1: Parent class
class Person:
    def __init__(self, name):
        self.name = name

# step2: Child class
class Teacher(Person): # Inheriting Person
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# step3: Display
    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}")

#step4: Creating object
if __name__ == "__main__":
    teacher = Teacher("Miss Saba", "Maths")
    teacher.display()