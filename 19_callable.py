class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value
    
if __name__ == "__main__":
    m = Multiplier(10)
    print("Result",m(5))  # Output: 50