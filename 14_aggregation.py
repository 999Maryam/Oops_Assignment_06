class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

    def show_employee(self):
        print(f"Employee Name: {self.employee.name}")

if __name__ == "__main__":
    emp = Employee("Maryam")
    dep = Department(emp)
    dep.show_employee()