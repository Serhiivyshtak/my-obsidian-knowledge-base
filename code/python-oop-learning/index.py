from datetime import date
from Apprentice import Apprentice
from Employee import Employee
        

first_apprentice = Apprentice("Serhii", "Vyshtak", "MATSE", 3, 15000, date(2006, 3, 28), date(2024, 9, 1))
second_apprentice = Apprentice("Vika", "Liubimka", "Kauffrau", 3, 20000, date(2025, 10, 12), date(2024, 9, 1))
third_apprentice = Apprentice("Anton", "Gandon", "Elektroniker", 2, 14000, date(2007, 9, 6), date(2025, 9, 1))

first_employee = Employee("Monika", "Swinka", "HR", 40000, date(1996, 3, 19), date(2020, 8, 27))
second_employee = Employee("Sven", "Bombastik", "Shef", 120000, date(1975, 12, 22), date(2009, 9, 1))

apprentices = [first_apprentice, second_apprentice, third_apprentice]
employees = [first_employee, second_employee]

for employee in apprentices + employees:
    print(employee)
    print("-----")

for apprentice in apprentices:
    apprentice.decrease_salary(1000)

for employee in employees:
    employee.increase_salary(3000)

for employee in apprentices + employees:
    print(employee)
    print("-----")


