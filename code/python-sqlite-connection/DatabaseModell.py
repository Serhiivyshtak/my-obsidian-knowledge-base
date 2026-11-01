import sqlite3


class DatabaseModell:
    def __init__(self, database_file_path):
        if  not isinstance(database_file_path, str):
            raise ValueError("Database file path should be a string")

        if database_file_path.strip() == "":
            raise ValueError("Database file path should not be empty")
        
        if not database_file_path.endswith((".db", ".sqlite", ".sqlite3")):
            raise ValueError("Database file should have a valid SQLite extension")

        self._database_file_path = database_file_path.strip()

        self._connection = sqlite3.connect(self._database_file_path)
        self._cursor = self._connection.cursor()

        self._cursor.execute("PRAGMA foreign_keys = ON")

        self._create_tables()


    def _create_tables(self):
        try:
            self._cursor.execute("""
                CREATE TABLE IF NOT EXISTS secundaries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name VARCHAR(100) NOT NULL,
                    second_name VARCHAR(100) NOT NULL,
                    birth_date DATE NOT NULL,
                    address VARCHAR(200) DEFAULT "unknown",
                    added_on DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            self._cursor.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text VARCHAR(1000) NOT NULL,
                    added_on DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
        except sqlite3.Error:
            raise RuntimeError("Uknown sqlite3 error occurred while creating tables")

        