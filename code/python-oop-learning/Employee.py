from datetime import date


class Employee:
    def __init__(self, first_name, last_name, profession, yearly_salary, birth_date, hire_date):
        if not isinstance(first_name, str):
            raise TypeError("First name can only be of the datatype str")

        if not isinstance(last_name, str):
            raise TypeError("Last name can only be of the datatype str")

        if not isinstance(profession, str):
            raise TypeError("Profession can only be of the datatype str")

        if not isinstance(yearly_salary, (float, int)):
            raise TypeError("Profession can only be of the datatype float")

        if not isinstance(birth_date, date):
            raise TypeError("Birth date can only be of the datatype date")

        if not isinstance(hire_date, date):
            raise TypeError("Hire date can only be of the datatype date")

        self._first_name = first_name
        self._last_name = last_name
        self._profession = profession
        self._yearly_salary = yearly_salary
        self._birth_date = birth_date
        self._hire_date = hire_date

    def __str__(self):
        return f"object from the class Employee\n- first_name: {self._first_name}\n- last_name: {self._last_name}\n- profession: {self._profession}\n- yearly_salary: {self._yearly_salary}\n- birth_date: {self._birth_date}\n- hire_date: {self._hire_date}"

    def increase_salary(self, salary_increase):
        self._yearly_salary += salary_increase

    def decrease_salary(self, salary_decrease):
        self._yearly_salary -= salary_decrease

    

        
