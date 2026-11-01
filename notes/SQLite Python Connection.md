# SQLite Python Connection

[Python] provides a built-in interface for working with SQLite databases through the *sqlite3 module*. This module is part of the Python standard library and therefore does not require separate installation. It enables developers to create, manage, and query relational databases directly within their Python applications without needing to set up an external database server.

The module implements the *DB-API 2.0* specification (PEP 249), a standardized set of interfaces for database access in Python. This means that the fundamental concepts and methods are transferable to other database systems as well.

## Fundamental Concepts

Working with SQLite in Python is based on two central objects: the *Connection* object and the *Cursor* object. The Connection object represents the connection to the database and manages transactions. The Cursor, on the other hand, is responsible for executing SQL commands and retrieving results.

A database can either be stored as a file on disk or kept as an *in-memory database* in RAM. The latter is particularly suitable for testing or temporary data processing, as it is automatically deleted when the connection is closed.

## Establishing a Connection

The first step when working with SQLite is establishing a database connection. The function `sqlite3.connect()` opens an existing database or automatically creates a new one if the specified file does not exist.

```python
import sqlite3

# Connect to a database file
con = sqlite3.connect("my_database.db")

# Alternatively: Create an in-memory database
con = sqlite3.connect(":memory:")
```

After establishing the connection, a Cursor object is needed to execute SQL commands:

```python
cur = con.cursor()
```

## Creating Tables

With the Cursor, SQL commands can be executed using the `execute()` method. Creating a table is done through a `CREATE TABLE` statement:

```python
cur.execute(
    "CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT,
        age INTEGER
    )"
)
```

SQLite supports various data types, with the most important being *TEXT* for strings, *INTEGER* for whole numbers, *REAL* for floating-point numbers, and *BLOB* for binary data. Due to SQLite's flexible typing, specifying data types is optional but recommended for better documentation.

## Inserting Data

Inserting data is done with the SQL command `INSERT`. Using *placeholders* is essential to prevent SQL injection attacks. Python values should never be embedded directly into SQL strings.

```python
# Insert a single record using placeholders
cur.execute(
    "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
    ("John Smith", "john@example.com", 30)
)

# Insert multiple records at once
data = [
    ("Anna Schmidt", "anna@example.com", 25),
    ("Peter Miller", "peter@example.com", 35),
    ("Lisa Weber", "lisa@example.com", 28)
]
cur.executemany(
    "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
    data
)

# Save changes to the database
con.commit()
```

Calling `commit()` is crucial: without this command, changes are not permanently saved to the database. SQLite uses *transactions* to ensure data consistency.

## Querying Data

Retrieving data is done with the SQL command `SELECT`. After execution, various methods are available to process the results:

```python
# Query all users
cur.execute("SELECT name, email, age FROM users")

# Fetch a single result
first_row = cur.fetchone()
print(first_row)  # Returns a tuple: ('John Smith', 'john@example.com', 30)

# Fetch all results as a list
cur.execute("SELECT name, email, age FROM users")
all_rows = cur.fetchall()

# Iterate over results
for row in cur.execute("SELECT name, age FROM users ORDER BY age"):
    print(f"{row[0]} is {row[1]} years old")
```

The three most important methods for fetching results are:

- `fetchone()` returns the next row as a tuple or `None` if no more rows are available
- `fetchall()` returns all remaining rows as a list of tuples
- `fetchmany(size)` returns a specified number of rows

## Updating and Deleting Data

Updating and deleting records is done with the SQL commands `UPDATE` and `DELETE`:

```python
# Update a record
cur.execute(
    "UPDATE users SET email = ? WHERE name = ?",
    ("newemail@example.com", "John Smith")
)

# Delete a record
cur.execute("DELETE FROM users WHERE name = ?", ("Peter Miller",))

# Save changes
con.commit()
```

## Error Handling

The sqlite3 module defines various *exceptions* for different error situations:

- `sqlite3.Error` is the base class for all sqlite3 errors
- `sqlite3.DatabaseError` occurs for database-related errors
- `sqlite3.IntegrityError` is raised when integrity constraints are violated
- `sqlite3.OperationalError` signals problems in database operations

Robust error handling could look like this:

```python
import sqlite3

try:
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (name) VALUES (?)", ("Test",))
    con.commit()
except sqlite3.IntegrityError as e:
    print(f"Integrity error: {e}")
except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    con.close()
```

## Properly Releasing Resources

After completing database operations, the connection should be closed to release resources. The recommended method is using the *context manager* with the `with` statement:

```python
import sqlite3

# Recommended approach with context manager
with sqlite3.connect("database.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    results = cur.fetchall()
    # commit() is automatically called upon successful exit from the block
```

Alternatively, the connection can be closed manually:

```python
con.close()
```

Starting with Python 3.13, a warning is issued if a Connection object is deleted without calling `close()`.

## Complete Example

The following example demonstrates a typical workflow with SQLite in Python:

```python
import sqlite3

# Establish database connection
con = sqlite3.connect("library.db")
cur = con.cursor()

# Create table
cur.execute("
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        year INTEGER,
        rating REAL
    )"
)

# Insert data
books = [
    ("The Trial", "Franz Kafka", 1925, 4.5),
    ("Faust", "Johann Wolfgang von Goethe", 1808, 4.8),
    ("The Metamorphosis", "Franz Kafka", 1915, 4.3)
]
cur.executemany(
    "INSERT INTO books (title, author, year, rating) VALUES (?, ?, ?, ?)",
    books
)
con.commit()

# Query data
print("All books by Kafka:")
for row in cur.execute(
    "SELECT title, year FROM books WHERE author LIKE ? ORDER BY year",
    ("%Kafka%",)
):
    print(f"  {row[0]} ({row[1]})")

# Close connection
con.close()
```

## Summary

The sqlite3 module provides a straightforward way to integrate relational databases into Python applications. The key points for practical use are:

- The module is part of the standard library and requires no installation
- Placeholders (`?`) must be used to prevent SQL injection
- After write operations, `commit()` must be called
- Resources should be released with `close()` or the context manager
- SQLite's dynamic type system allows flexible data structures

---

*Sources: [Python sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html), [W3Schools Python sqlite3](https://www.w3schools.com/python/ref_module_sqlite3.asp)*
