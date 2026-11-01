# Python Basic Syntax Guide

## Variables

In [Python], a *variable* is a name that refers to a value stored in memory. Unlike many other programming languages, Python does not require you to declare the type of a variable before using it. The type is determined automatically based on the value you assign.

To create a variable, you simply write a name followed by an equals sign and the value you want to store. For example, `age = 25` creates a variable called `age` that holds the integer value 25. Variable names must start with a letter or underscore, cannot contain spaces, and are case-sensitive, meaning `Name` and `name` are two different variables.

Python supports several basic data types. *Integers* are whole numbers like `42` or `-7`. *Floats* are decimal numbers like `3.14` or `-0.5`. *Strings* are sequences of characters enclosed in single or double quotes, such as `"Hello"` or `'World'`. *Booleans* represent truth values and can only be `True` or `False`.

```python
name = "Alice"
age = 30
height = 1.75
is_student = True
```

You can change the value of a variable at any time by assigning a new value to it. Python also allows you to assign values to multiple variables in a single line using `x, y, z = 1, 2, 3`.

## Operators

*Operators* are symbols that perform operations on values and variables. Python provides several categories of operators for different purposes.

*Arithmetic operators* perform mathematical calculations. The plus sign `+` adds numbers, the minus sign `-` subtracts them, the asterisk `*` multiplies, and the forward slash `/` divides. The double asterisk `**` raises a number to a power, so `2 ** 3` equals 8. The double forward slash `//` performs floor division, which divides and rounds down to the nearest integer. The percent sign `%` is the modulo operator, which returns the remainder after division.

```python
result = 10 + 5      # Addition: 15
result = 10 - 5      # Subtraction: 5
result = 10 * 5      # Multiplication: 50
result = 10 / 3      # Division: 3.333...
result = 10 // 3     # Floor division: 3
result = 10 % 3      # Modulo: 1
result = 2 ** 4      # Exponentiation: 16
```

*Comparison operators* compare two values and return a boolean result. The double equals sign `==` checks if values are equal, while `!=` checks if they are not equal. The symbols `<`, `>`, `<=`, and `>=` compare whether values are less than, greater than, less than or equal to, or greater than or equal to each other.

*Logical operators* combine boolean expressions. The keyword `and` returns True only if both conditions are true. The keyword `or` returns True if at least one condition is true. The keyword `not` inverts a boolean value.

```python
x = 5
print(x > 3 and x < 10) # True
print(x > 3 or x > 10) # True
print(not(x > 3)) # False
```

## Console Input and Output

*Output* in Python is handled primarily through the `print()` function, which displays information to the console. You can pass any value or variable to this function, and it will convert it to text and display it.

```python
print("Hello, World!")
print(42)
print("The answer is", 42)
```

When you pass multiple values to `print()` separated by commas, Python automatically inserts spaces between them. You can customize the separator using the `sep` parameter and change what appears at the end of the output using the `end` parameter. By default, `print()` adds a newline character at the end.

```python
print("apple", "banana", "cherry", sep=", ") # Output: apple, banana, cherry
print("Hello", end=" ")
print("World") # Output: Hello World
```

*Formatted strings*, also called *f-strings*, allow you to embed variables directly inside strings by prefixing the string with the letter `f` and placing variables inside curly braces.

```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

*Input* is handled through the `input()` function, which pauses the program and waits for the user to type something and press Enter. The function always returns the entered value as a string, so you must convert it to another type if needed.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
```

The `int()` function converts a string to an integer, and the `float()` function converts it to a decimal number. If the user enters something that cannot be converted, the program will crash with an error.

## If-Elif-Else Expressions

*Conditional statements* allow your program to make decisions and execute different code based on whether certain conditions are true or false. The most basic form is the `if` statement, which executes a block of code only if a specified condition evaluates to True.

```python
age = 18

if age >= 18:
    print("You are an adult.")
```

The code that belongs to the `if` statement must be indented with spaces or tabs. This indentation is not optional in Python; it defines which lines of code are part of the conditional block.

The `else` keyword provides an alternative block of code that executes when the `if` condition is False.

```python
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

When you need to check multiple conditions, use `elif`, which is short for "else if". Python evaluates each condition in order and executes only the first block whose condition is True.

```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

You can also nest conditional statements inside each other and combine multiple conditions using logical operators.

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("You need a license to drive.")
else:
    print("You are too young to drive.")
```

## Loops

*Loops* allow you to execute a block of code repeatedly, either a specific number of times or while a certain condition remains true.

The *for loop* iterates over a sequence of values. The most common way to create a sequence of numbers is with the `range()` function. Calling `range(5)` produces the numbers 0, 1, 2, 3, 4. You can also specify a starting value and a step size with `range(start, stop, step)`.

```python
for i in range(5):
    print(i) # Prints 0, 1, 2, 3, 4

for i in range(2, 10, 2):
    print(i) # Prints 2, 4, 6, 8
```

For loops can iterate over any sequence, including strings and lists.

```python
for letter in "Python":
    print(letter) # Prints each letter on a new line

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

The *while loop* continues executing as long as its condition remains True. Be careful to ensure that the condition eventually becomes False, or the loop will run forever.

```python
count = 0

while count < 5:
    print(count)
    count += 1 # Same as count = count + 1
```

The `break` statement immediately exits the loop, regardless of the loop condition. The `continue` statement skips the rest of the current iteration and moves to the next one.

```python
for i in range(10):
    if i == 3:
        continue # Skip printing 3

    if i == 7:
        break # Stop the loop entirely at 7

    print(i) # Prints 0, 1, 2, 4, 5, 6
```

## Functions

A *function* is a reusable block of code that performs a specific task. Functions help organize code, avoid repetition, and make programs easier to understand and maintain.

You define a function using the `def` keyword, followed by the function name, parentheses, and a colon. The code inside the function must be indented.

```python
def greet():
    print("Hello, World!")

greet() # Call the function
```

*Parameters* are variables listed inside the parentheses when defining a function. They act as placeholders for values that will be passed in when the function is called. The actual values passed are called *arguments*.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice") # Output: Hello, Alice!
greet("Bob") # Output: Hello, Bob!
```

Functions can have multiple parameters and can also have *default values*, which are used when no argument is provided.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice") # Output: Hello, Alice!
greet("Bob", "Good morning") # Output: Good morning, Bob!
```

The `return` statement sends a value back to the code that called the function. A function can return any type of value, and once a return statement is executed, the function stops immediately.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result) # 8
```

Functions can return multiple values as a *tuple*, which you can unpack into separate variables.

```python
def get_dimensions():
    return 1920, 1080

width, height = get_dimensions()
print(f"Width: {width}, Height: {height}")
```

*Variable scope* determines where a variable can be accessed. Variables created inside a function are *local* and cannot be accessed outside it. Variables created outside functions are *global* and can be read inside functions, but to modify them you must use the `global` keyword.

```python
counter = 0 # Global variable

def increment():
    global counter
    counter += 1

increment()
print(counter) # 1
```

## Try-Except Expressions

*Exception handling* allows your program to deal with errors gracefully instead of crashing. When Python encounters an error during execution, it creates an *exception* object. If this exception is not handled, the program terminates and displays an error message.

The `try` block contains code that might cause an error. The `except` block contains code that runs if an error occurs. This structure allows your program to continue running even when something goes wrong.

```python
try:
    number = int(input("Enter a number: "))
    print(f"You entered {number}")
except:
    print("That was not a valid number.")
```

You can specify which type of exception to catch, which is considered better practice because it only handles expected errors and lets unexpected ones surface for debugging.

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Common exception types include *ValueError* for invalid value conversions, *TypeError* for operations on incompatible types, *IndexError* for accessing list indices that do not exist, *KeyError* for accessing dictionary keys that do not exist, and *FileNotFoundError* for attempting to open files that do not exist.

The `else` block runs only if no exception occurred in the try block. The `finally` block always runs, regardless of whether an exception occurred, and is typically used for cleanup operations.

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
else:
    print("File read successfully.")
    print(content)
finally:
    print("Operation complete.")
```

You can capture the exception object to access more information about what went wrong.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
```

You can also raise your own exceptions using the `raise` keyword when you want to signal that something has gone wrong in your code.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age

try:
    user_age = set_age(-5)
except ValueError as e:
    print(e) # Output: Age cannot be negative.
```
