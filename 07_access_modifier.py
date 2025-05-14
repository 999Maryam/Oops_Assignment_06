class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name # Public
        self._salary = salary # Protected
        self.__ssn = ssn # Private

emp = Employee("Maryam", 50000, "123-45678-9")

print(emp.name)
print(emp._salary)
print(emp.__ssn)