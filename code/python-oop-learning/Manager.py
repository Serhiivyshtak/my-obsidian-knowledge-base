from Employee import Employee


class Manager:
    def __init__(self, first_name, last_name, profession, yearly_salary, birth_date, hire_date, employees_under_management):
        super().__init__(first_name, last_name, profession, yearly_salary, birth_date, hire_date)

        if not isinstance(employees_under_management, list):
            raise TypeError("'employees_under_management' variable should be an array")

        for employee in employees_under_management:
            if not isinstance(employee, Employee):
                raise TypeError("Each item in 'employees_under_management' list should be an object of 'Employee instance'")

        self._employees_under_management = employees_under_management

    def __str__(self):
            return f"object from the class Manager\n- first_name: {self._first_name}\n- last_name: {self._last_name}\n- profession: {self._profession}\n- yearly_salary: {self._yearly_salary}\n- birth_date: {self._birth_date}\n- hire_date: {self._hire_date}"
         
        