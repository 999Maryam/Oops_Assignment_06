def add_greeting(cls):
    def greet(self):
        return "Hello from decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    p = Person("John")
    print(p.greet())  # Output: Hello from decorator!