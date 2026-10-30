from datetime import date
from abc import ABC, abstractmethod


class Employee(ABC):
    employees_count = 0

    def __init__(self, first_name, last_name, profession, yearly_salary, birth_date, hire_date):
        if not isinstance(first_name, str):
            raise TypeError("'first_name' should be an str")

        if not isinstance(last_name, str):
            raise TypeError("'last_name' should be an str")

        if not isinstance(profession, str):
            raise TypeError("'profession' should be an str")

        if not isinstance(yearly_salary, (float, int)):
            raise TypeError("'yearly_salary' should be a float or int")

        if not isinstance(birth_date, date):
            raise TypeError("'birth_date' should be a date")

        if not isinstance(hire_date, date):
            raise TypeError("'hire_date' should be a date")

        self._first_name = first_name
        self._last_name = last_name
        self._profession = profession
        self._yearly_salary = yearly_salary
        self._birth_date = birth_date
        self._hire_date = hire_date

        Employee.employees_count += 1

    def increase_salary(self, salary_increase):
        self._yearly_salary += salary_increase
    
    def decrease_salary(self, salary_decrease):
        self._yearly_salary -= salary_decrease

    @property
    def yearly_salary(self):
        return self._yearly_salary

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @abstractmethod
    def __str__(self):
        pass
    

        
