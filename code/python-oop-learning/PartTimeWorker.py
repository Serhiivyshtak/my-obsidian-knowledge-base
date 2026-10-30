from Employee import Employee


class PartTimeWorker(Employee):
    def __init__(self, first_name, last_name, profession, yearly_salary, birth_date, hire_date, hourly_rate, benefits):
        super().__init__(first_name, last_name, profession, yearly_salary, birth_date, hire_date)

        if not isinstance(hourly_rate, (int, float)):
            raise TypeError("'hourly_rate' should be a either int or float")

        if not isinstance(benefits, list):
            raise TypeError("'benefits' should be a list")

        for benefit in benefits:
            if not isinstance(benefit, str):
                raise TypeError("Each item in 'benefits' list should be a string")

        self._hourly_rate = hourly_rate
        self._benefits = benefits

    def __str__(self):
        return f"object from the class PartTimeWorker\n- first_name: {self._first_name}\n- last_name: {self._last_name}\n- profession: {self._profession}\n- yearly_salary: {self._yearly_salary}\n- birth_date: {self._birth_date}\n- hire_date: {self._hire_date}\n- hourly_rate: {self._hourly_rate}\n- benefits: {self._benefits}"