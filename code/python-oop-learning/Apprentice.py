from Employee import Employee


class Apprentice(Employee):
    def __init__(self, first_name, last_name, profession, yearly_salary, birth_date, hire_date, apprenticeship_year):
        super().__init__(first_name, last_name, profession, yearly_salary, birth_date, hire_date)

        if not isinstance(apprenticeship_year, int):
            raise TypeError("'apprenticeship_year' should be an int")
        
        self._apprenticeship_year = apprenticeship_year

    def __str__(self):
        return f"object from the class Apprentice\n- first_name: {self._first_name}\n- last_name: {self._last_name}\n- profession: {self._profession}\n- yearly_salary: {self._yearly_salary}\n- apprenticeship_year: {self._apprenticeship_year}\n- birth_date: {self._birth_date}\n- hire_date: {self._hire_date}"