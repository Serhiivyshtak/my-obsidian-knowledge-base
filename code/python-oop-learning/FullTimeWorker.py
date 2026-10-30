from Employee import Employee

class FullTimeWorker(Employee):
    def __init__(self, first_name, last_name, profession, yearly_salary, birth_date, hire_date, benefits):
        super().__init__(first_name, last_name, profession, yearly_salary, birth_date, hire_date)

        if not isinstance(benefits, list):
            raise TypeError("'benefits' should be a list")

        for benefit in benefits:
            if not isinstance(benefit, str):
                raise TypeError("Each item in 'benefits' list should be a string")

        self._benefits = benefits

    def __str__(self):
        return f"object from the class FullTimeWorker\n- first_name: {self._first_name}\n- last_name: {self._last_name}\n- profession: {self._profession}\n- yearly_salary: {self._yearly_salary}\n- birth_date: {self._birth_date}\n- hire_date: {self._hire_date}\n- benefits: {self._benefits}"