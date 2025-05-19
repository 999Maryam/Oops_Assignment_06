class TemperatureConvertor:

    @staticmethod
    def convert_celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
if __name__ == "__main__":
    print(f"Fahrenheit:",TemperatureConvertor.convert_celsius_to_fahrenheit(0))
    print(f"Fahrenheit:",TemperatureConvertor.convert_celsius_to_fahrenheit(100))

