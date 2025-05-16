class Dog:
    def __init__(self, name, breed):
        self.name = name   #Instance variable
        self.breed = breed #Instance variable

    def bark(self): #Instance method
        print(f"{self.name},{self.breed} says Woof")

if __name__ == "__main__":
    #Creating object(Instance)
    my_dog = Dog("Bob","German Shepherd")
    my_dog.bark() #Call the instance method
    