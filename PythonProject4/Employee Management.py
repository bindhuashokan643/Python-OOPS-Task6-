# Employee Management

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_Salary(self):
        return self.salary

#Subclass : Regular Employee

class RegularEmployee(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_Salary(self):
        total = self.salary
        print(self.name, "salary is", total)

#Subclass : Contract Employee

class ContractEmployee:
    def __init__(self, name, hours, rate):
         self.name = name
         self.hours = hours
         self.rate = rate

    def calculate_HourlyRate(self):
        total = self.hours * self.rate
        print(self.name, "salary is", total)

#Subeclass: Manager

class Manager(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_Salary(self):
        total = self.salary
        print(self.name, "salary is", total)

# Create objects

emp1 = RegularEmployee("Pooja", 10000)
emp2 = ContractEmployee("Vrushali", 2000, 0.10)
emp3 = Manager(name="Bindhu", salary=10000)


#call method

emp1.calculate_Salary()
emp2.calculate_HourlyRate()
emp3.calculate_Salary()