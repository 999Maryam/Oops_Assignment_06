class Engine:
    def start (self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine() # Composition

    def car_start(self):
        self.engine.start()
        print("Car is ready to go")
    
if __name__ == "__main__":
    my_car = Car()
    my_car.car_start()
