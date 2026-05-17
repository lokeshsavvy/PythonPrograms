class Employee:
    def __init__(self,name,salary):
            self.name = name
            self.salary = salary
    def calculate_salary(self):
            return self.salary
class RegularEmployee(Employee):
    def __init__(self,name,salary):
            super().__init__(name,salary)
class ContractEmployee(Employee):
    def __init__(self,name,hours,rate):
            super().__init__(name,0)
            self.hours = hours
            self.rate = rate
    def calculate_salary(self):
            return self.hours * self.rate
class Manager(Employee):
    def __init__(self,name,salary,bonus):
            super().__init__(name,salary)
            self.bonus = bonus
    def calculate_salary(self):
            return self.salary + self.bonus
            
#creating object and taking inputs from the user

emp_data = input("Enter the employee type: ").lower()
if emp_data == 'regular':
    name = input("Enter the name: ")
    salary = int(input("Enter the salary: "))
    obj = RegularEmployee(name,salary)
elif emp_data == 'contract':
    name = input("Enter the name: ")
    hours = int(input("Enter the hours: "))
    rate = int(input("Enter the rate: "))
    obj = ContractEmployee(name,hours,rate)
elif emp_data == "manager":

    name = input("Enter the name: ")
    salary = int(input("Enter the salary: "))
    bonus = int(input("Enter the bonus: "))
    obj = Manager(name,salary,bonus)
else:
    print("invalid employe input")
print(obj.calculate_salary())













