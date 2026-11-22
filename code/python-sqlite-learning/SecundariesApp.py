from DatabaseModell import DatabaseModell
from datetime import date


class SecundariesApp(DatabaseModell):
    def __init__(self, database_file_path):
        super().__init__(database_file_path)

        self._available_actions = [
            {"description": "Show all Secundaries", "func": self.show_all_secundaries},
            {"description": "Append a new Secundary", "func": self.append_secundary},
            {"description": "Show information related to a specific Secundary", "func": self.show_secundary_info},
            {"description": "Remove a Secundary", "func": self.remove_secundary},
        ]


    # --------------------------------------------------------------------------------------------------------
    def show_all_secundaries(self) -> None:
        try:
            secundaries = self.db_fetch_all_secundaries()
        except RuntimeError as error:
            print(f"RUNTIME ERROR -> {error}")
            return

        if len(secundaries) == 0:
            print("No Secundaries added yet")
            return

        print("All available Secundaries:")
        
        for secundary in secundaries:
            print(f"- {secundary[1]} {secundary[2]} {secundary[3]} (Id: {secundary[0]})")


    # --------------------------------------------------------------------------------------------------------
    def append_secundary(self) -> None:
        print("To append a new Secundary enter all the needed information below")

        first_name = input("Secundary's first name: ")

        while first_name.strip() == "":
            print("First name shouldn't be empty")
            first_name = input("Secundary's first name: ")

        second_name = input("Secundary's second name: ")

        while second_name.strip() == "":
            print("Second name shouldn't be empty")
            second_name = input("Secundary's second name: ")

        birthdate = input("Secundary's birthdate (YYYY-MM-DD): ")

        valid_birthdate = False

        while not valid_birthdate:
            try:
                birthdate_year = int(birthdate[0:4])
                birthdate_month = int(birthdate[5:7])
                birthdate_day = int(birthdate[8:10])

                birthdate_as_date = date(birthdate_year, birthdate_month, birthdate_day)

                valid_birthdate = True
            except ValueError:
                print("Invalid date were given")
                birthdate = input("Secundary's birthdate (YYYY-MM-DD): ")

        address = input("Secundary's address (not required): ")
        phone_number = input("Secundary's phone number (not required): ")

        if address.strip() == "":
            address = "unknown"

        if phone_number.strip() == "":
            phone_number = "unknown"

        try:
            self.db_append_secundary(first_name, second_name, birthdate_as_date, address, phone_number)
        except ValueError as error:
            print(f"VALUE ERROR -> {error}")
        except RuntimeError as error:
            print(f"RUNTIME ERROR -> {error}")
            return

        print(f"Secundary {first_name} {second_name} has been added")


    # --------------------------------------------------------------------------------------------------------
    def show_secundary_info(self) -> None:
        print("To see information related to a specific Secundary enter the corresponding identifier below")

        id = input("Secundary's identifier: ")

        id_valid = False

        while not id_valid:
            try: 
                parsed_id = int(id)
                id_valid = True
            except ValueError:
                print("Identifier should be an integer")
                id = input("Secundary's identifier: ")

        try:
            secundary = self.db_fetch_secundary(parsed_id)
        except ValueError as error:
            print(f"VALUE ERROR -> {error}")
            return
        except RuntimeError as error:
            print(f"RUNTIME ERROR -> {error}")
            return

        if secundary == None:
            print("There is no Secundary with such an identifier")
            return

        print(f"- Full name: {secundary[1]} {secundary[2]}\n- Birthdate: {secundary[3]}\n- Address: {secundary[4]}\n- Phone number: {secundary[5]}")


    # --------------------------------------------------------------------------------------------------------
    def remove_secundary(self):
        print("To remove a Secundary enter the corresponding identifier below")

        id = input("Secundary's identifier: ")
        
        id_valid = False

        while not id_valid:
            try: 
                parsed_id = int(id)
                id_valid = True
            except ValueError:
                print("Identifier should be an integer")
                id = input("Secundary's identifier: ")

        try:
            secundary = self.db_fetch_secundary(parsed_id)
        except ValueError as error:
            print(f"VALUE ERROR -> {error}")
            return
        except RuntimeError as error:
            print(f"RUNTIME ERROR -> {error}")
            return

        if secundary == None:
            print("There is no Secundary with such an identifier")
            return

        try:
            self.db_remove_secundary(parsed_id)
        except ValueError as error:
            print(f"VALUE ERROR -> {error}")
            return
        except RuntimeError as error:
            print(f"RUNTIME ERROR -> {error}")
            return

        print(f"Secundary with the identifier {parsed_id} ({secundary[1]} {secundary[2]}) has been removed")


    # --------------------------------------------------------------------------------------------------------
    @property
    def available_actions(self):
        return self._available_actions