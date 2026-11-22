import sqlite3
from datetime import date


class DatabaseModell:
    def __init__(self, database_file_path):
        if  not isinstance(database_file_path, str):
            raise ValueError("'database_file_path' should be a string")

        if database_file_path.strip() == "":
            raise ValueError("'database_file_path' shouldn't be empty")
        
        if not database_file_path.endswith((".db", ".sqlite", ".sqlite3")):
            raise ValueError("Database file should have a valid SQLite extension")

        self._database_file_path = database_file_path.strip()

        try:
            self._connection = sqlite3.connect(self._database_file_path)
            self._cursor = self._connection.cursor()
            self._cursor.execute("PRAGMA foreign_keys = ON")
        except sqlite3.Error as error:
            raise RuntimeError(f"Sqlite error occured while initilizing connection -> {error}")

        try:
            self._create_tables()
        except sqlite3.Error as error:
            raise RuntimeError(f"Sqlite3 error occurred while creating tables -> {error}")

    # --------------------------------------------------------------------------------------------------------
    def _create_tables(self) -> None:
        self._cursor.execute("""
            CREATE TABLE IF NOT EXISTS secundaries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name VARCHAR(100) NOT NULL,
                second_name VARCHAR(100) NOT NULL,
                birth_date DATE NOT NULL,
                address VARCHAR(200) DEFAULT "unknown",
                phone_number VARCHAR(100) DEFAULT "unknown",
                added_on DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


    # --------------------------------------------------------------------------------------------------------
    def db_fetch_all_secundaries(self) -> list:
        """
            Fetches all available secundaries from the database. 
        """

        try:
            self._cursor.execute("""
                SELECT * FROM secundaries
            """)

            return self._cursor.fetchall()
        except sqlite3.Error as error:
            raise RuntimeError(f"Sqlite3 error occurred while fetching the secundaries -> {error}")


    # --------------------------------------------------------------------------------------------------------
    def db_append_secundary(self, first_name: str, second_name: str, birth_date: date, address: str, phone_number: str) -> None:
        """
            Appends a new secundary to the database
        """

        if not isinstance(first_name, str):
            raise ValueError("'first_name' should be an instance of str")

        if not isinstance(second_name, str):
            raise ValueError("'second_name' should be an instance of str")

        if not isinstance(birth_date, date):
            raise ValueError("'birth_date' should be an instance of date")

        if not isinstance(address, str):
            raise ValueError("'address' should be an instance of str")

        if not isinstance(phone_number, str):
            raise ValueError("'phone_number' should be an instance of str")

        try:
            self._cursor.execute("""
                INSERT INTO secundaries (first_name, second_name, birth_date, address, phone_number) VALUES (?, ?, ?, ?, ?)
            """, (first_name, second_name, birth_date, address, phone_number))
            self._connection.commit()
        except sqlite3.Error as error:
            raise RuntimeError(f"Sqlite3 error occurred while appending a secundary -> {error}")


    # --------------------------------------------------------------------------------------------------------
    def db_fetch_secundary(self, id: int) -> tuple:
        """
            Fetches one secundary from the database based on id
        """

        if not isinstance(id, int):
            raise ValueError("'id' should be an instance of int")

        try:
            self._cursor.execute("SELECT * FROM secundaries WHERE id = ?", (id,))
            return self._cursor.fetchone()
        except sqlite3.Error as error:
            raise RuntimeError(f"Sqlite3 error occurred while fetching a secundary -> {error}")


    # --------------------------------------------------------------------------------------------------------
    def db_remove_secundary(self, id: int) -> None:
        """
            Removes one secundary based on id
        """

        if not isinstance(id, int):
            raise ValueError("'id' should be an instance of int")

        try:
            self._cursor.execute("DELETE FROM secundaries WHERE id = ?", (id,))
            self._connection.commit()
        except sqlite3.Error as error:
            raise RuntimeError(f"Sqlite3 error occurred while deleting a secundary -> {error}")

    
        

        

        