from datetime import date
from Apprentice import Apprentice
from Employee import Employee
from FullTimeWorker import FullTimeWorker
from PartTimeWorker import PartTimeWorker
from Manager import Manager


print(Employee.employees_count)
print()

first_employee = FullTimeWorker("Monika", "Swinka", "HR", 40000, date(1996, 3, 19), date(2020, 8, 27), ["Health Insurance", "Paid Time Off"])
second_employee = FullTimeWorker("John", "Doe", "Engineer", 50000, date(1990, 5, 15), date(2018, 6, 1), ["Health Insurance", "Paid Time Off"])
third_employee = Apprentice("Alice", "Smith", "Intern", 20000, date(2000, 7, 10), date(2023, 1, 15), 2)
fourth_employee = Apprentice("Bob", "Johnson", "Intern", 18000, date(2001, 2, 20), date(2023, 2, 1), 1)
fifth_employee = PartTimeWorker("Charlie", "Brown", "Consultant", 30000, date(1985, 11, 5), date(2015, 4, 10), 20, ["Health Insurance"])
sixth_employee = Manager("Diana", "Prince", "Manager", 80000, date(1988, 4, 25), date(2010, 9, 15), [first_employee, second_employee, third_employee, fourth_employee, fifth_employee])

print(Employee.employees_count)
print()

all_employees = [first_employee, second_employee, third_employee, fourth_employee, fifth_employee, sixth_employee]

for employee in all_employees:
    print(employee)
    print()

    if isinstance(employee, Apprentice):
        employee.increase_salary(2000)
    else:
        employee.increase_salary(5000)


for employee in all_employees:
    print(employee)
    print()


