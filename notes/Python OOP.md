# Object-Oriented Programming in Python

## Classes and Objects

A *class* is a template or blueprint that describes what properties and capabilities objects of a certain type should have. You can think of a class as a mold from which concrete objects are created.

An *object* (also called an *instance*) is a concrete specimen created according to the blueprint of a class. While a class only defines the structure, an object contains actual values.

In [Python], you define a class with the `class` keyword, followed by the class name. By convention, the class name begins with an uppercase letter.

```python
class Car:
    pass
```

To create an object, you call the class like a function.

```python
my_car = Car()
another_car = Car()
```

Each created object is independent of other objects of the same class. You can create as many objects from a class as you like.

## The Constructor and Attributes

The *constructor* is a special method that is automatically called when a new object is created. In Python, this method is called `__init__`. It serves to initialize an object with initial values.

*Attributes* are variables that belong to an object and store its properties. They are defined within the constructor and prefixed with `self`.

```python
class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
        self.speed = 0
```

The `self` keyword refers to the current object. It must be specified as the first parameter in every method of a class and allows access to the object's attributes and methods.

When creating an object, you pass the values for the constructor's parameters.

```python
my_car = Car("Volkswagen", "blue", 2020)
print(my_car.brand)           # Volkswagen
print(my_car.color)           # blue
print(my_car.year)            # 2020
```

You can read and modify attributes at any time.

```python
my_car.color = "red"
print(my_car.color)           # red
```

## Methods

*Methods* are functions defined within a class that describe the behavior of objects. They have access to the object's attributes through `self`.

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0
    
    def accelerate(self, value):
        self.speed += value
        print(f"The car accelerates to {self.speed} km/h.")
    
    def brake(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0
        print(f"The car brakes to {self.speed} km/h.")
    
    def info(self):
        return f"{self.brand} in {self.color}, currently {self.speed} km/h"
```

Methods are called on an object using dot notation.

```python
my_car = Car("BMW", "black")
my_car.accelerate(50)         # The car accelerates to 50 km/h.
my_car.accelerate(30)         # The car accelerates to 80 km/h.
my_car.brake(20)              # The car brakes to 60 km/h.
print(my_car.info())          # BMW in black, currently 60 km/h
```

## Encapsulation

*Encapsulation* is the principle of hiding the internal details of an object and providing only a controlled interface to the outside. This protects data from unintended changes and makes the code more robust.

In Python, there is no true access control as in other languages. Instead, naming conventions are used. An underscore before an attribute name (`_attribute`) signals that the attribute should be considered *internal* and should not be accessed from outside.

```python
class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self._balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} euros deposited. New balance: {self._balance} euros")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"{amount} euros withdrawn. New balance: {self._balance} euros")
        else:
            print("Withdrawal not possible.")
    
    def get_balance(self):
        return self._balance
```

Two underscores (`__attribute`) lead to *name mangling*, making the attribute harder to access from outside. Python internally changes the name to `_Classname__attribute`.

```python
class Secret:
    def __init__(self):
        self.__secret_data = "confidential"
    
    def show_secret(self):
        return self.__secret_data

obj = Secret()
# print(obj.__secret_data)              # AttributeError
print(obj._Secret__secret_data)         # confidential (technically possible, but not recommended)
print(obj.show_secret())                # confidential
```

## Properties

*Properties* provide an elegant way to control access to attributes while maintaining the simple syntax of attribute access. They allow you to add getter and setter logic without changing the class interface.

The `@property` decorator defines a method as a getter. The `@attributename.setter` decorator defines the corresponding setter.

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value
    
    @property
    def name(self):
        return self._name
```

With properties, you can access attributes as usual while the defined methods are executed in the background.

```python
person = Person("Anna", 25)
print(person.age)             # 25
person.age = 26               # Setter is called
print(person.age)             # 26
# person.age = -5             # ValueError: Age cannot be negative.
```

## Inheritance

*Inheritance* allows you to create new classes based on existing classes. The new class (*child class* or *derived class*) inherits all attributes and methods from the existing class (*parent class* or *base class*) and can extend or override them.

The parent class is specified in parentheses after the child class name.

```python
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def start(self):
        print("The vehicle starts.")
    
    def info(self):
        return f"{self.brand}, year {self.year}"

class Car(Vehicle):
    def __init__(self, brand, year, number_of_doors):
        super().__init__(brand, year)
        self.number_of_doors = number_of_doors
    
    def honk(self):
        print("Honk!")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar
```

The `super()` function calls methods of the parent class. In the child class constructor, `super().__init__()` is typically used to execute the parent class constructor.

```python
my_car = Car("Audi", 2021, 4)
print(my_car.info())          # Audi, year 2021
my_car.start()                # The vehicle starts.
my_car.honk()                 # Honk!

my_motorcycle = Motorcycle("Harley", 2019, False)
my_motorcycle.start()         # The vehicle starts.
```

## Overriding Methods

A child class can *override* methods of the parent class by defining a method with the same name. When the method is called on an object of the child class, the overridden version is executed.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} barks: Woof woof!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} meows: Meow!")
```

```python
animal = Animal("Unknown")
dog = Dog("Buddy")
cat = Cat("Whiskers")

animal.make_sound()           # The animal makes a sound.
dog.make_sound()              # Buddy barks: Woof woof!
cat.make_sound()              # Whiskers meows: Meow!
```

You can also call the parent class method within the overridden method.

```python
class Bird(Animal):
    def make_sound(self):
        super().make_sound()
        print(f"{self.name} also chirps.")

bird = Bird("Tweety")
bird.make_sound()
# Output:
# The animal makes a sound.
# Tweety also chirps.
```

## Polymorphism

*Polymorphism* means that different objects can respond differently to the same message. In Python, this allows functions to work with objects of different classes as long as those classes implement the expected methods.

```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says Woof!"

class Cat:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says Meow!"

class Cow:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says Moo!"
```

A function can work with any objects that have the expected method. This is called *duck typing*: "If it looks like a duck and quacks like a duck, then it probably is a duck."

```python
def make_animal_speak(animal):
    print(animal.speak())

animals = [Dog("Buddy"), Cat("Whiskers"), Cow("Bessie")]

for animal in animals:
    make_animal_speak(animal)

# Output:
# Buddy says Woof!
# Whiskers says Meow!
# Bessie says Moo!
```

## Class Attributes and Class Methods

*Class attributes* are variables that belong to the class itself and are shared by all instances. They are defined directly in the class, outside the constructor.

```python
class Employee:
    company = "TechCorp"
    employee_count = 0
    
    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1
    
    def info(self):
        return f"{self.name} works at {Employee.company}"
```

```python
e1 = Employee("Anna")
e2 = Employee("Ben")
e3 = Employee("Clara")

print(Employee.employee_count)        # 3
print(e1.info())                      # Anna works at TechCorp
```

*Class methods* are methods that operate on the class rather than on an instance. They are marked with the `@classmethod` decorator and receive `cls` (the class itself) as the first parameter instead of `self`.

```python
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    @classmethod
    def from_string(cls, date_string):
        day, month, year = map(int, date_string.split("."))
        return cls(day, month, year)
    
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
```

```python
date1 = Date(15, 6, 2023)
date2 = Date.from_string("24.12.2023")

print(date1)                  # 15.6.2023
print(date2)                  # 24.12.2023
```

## Static Methods

*Static methods* are functions defined in a class but do not need to access instance attributes or class attributes. They are marked with the `@staticmethod` decorator and receive neither `self` nor `cls` as a parameter.

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0
```

```python
print(Calculator.add(5, 3))           # 8
print(Calculator.multiply(4, 7))      # 28
print(Calculator.is_even(10))         # True
```

Static methods primarily serve to logically group functions into a class, even if they do not need object data.

## Magic Methods (Dunder Methods)

*Magic methods* (also called *dunder methods*, from "double underscore") are special methods with double underscores at the beginning and end of the name. They allow you to customize the behavior of objects during built-in Python operations.

The `__str__` method defines how an object is represented as a readable string when `print()` or `str()` is used.

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f'"{self.title}" by {self.author}'
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
```

```python
book = Book("The Trial", "Franz Kafka", 304)
print(book)                   # "The Trial" by Franz Kafka
print(repr(book))             # Book('The Trial', 'Franz Kafka', 304)
```

The `__repr__` method provides a technical representation that could ideally be used to recreate the object.

Other important magic methods enable comparisons and arithmetic operations.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
```

```python
v1 = Vector(3, 4)
v2 = Vector(1, 2)

v3 = v1 + v2
print(v3)                     # Vector(4, 6)

v4 = v1 - v2
print(v4)                     # Vector(2, 2)

print(v1 == Vector(3, 4))     # True
print(len(v1))                # 5
```

The most important magic methods are:

- `__init__`: Constructor, initializes a new object
- `__str__`: Readable string for `print()` and `str()`
- `__repr__`: Technical representation for developers
- `__len__`: Called for `len(object)`
- `__eq__`: Comparison with `==`
- `__lt__`, `__gt__`, `__le__`, `__ge__`: Comparisons with `<`, `>`, `<=`, `>=`
- `__add__`, `__sub__`, `__mul__`, `__truediv__`: Arithmetic operations

## Abstract Classes

An *abstract class* is a class that cannot be instantiated directly and serves as a template for other classes. It defines methods that must be implemented by all child classes.

In Python, abstract classes are created using the `abc` module (Abstract Base Classes).

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def description(self):
        return "This is a geometric shape."
```

Any class that inherits from an abstract class must implement all abstract methods.

```python
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
```

```python
# shape = Shape()               # TypeError: Can't instantiate abstract class

rectangle = Rectangle(5, 3)
print(rectangle.area())           # 15
print(rectangle.perimeter())      # 16
print(rectangle.description())    # This is a geometric shape.

circle = Circle(4)
print(circle.area())              # 50.26...
print(circle.perimeter())         # 25.13...
```

## Multiple Inheritance

Python supports *multiple inheritance*, where a class can inherit from multiple parent classes. This allows combining functionality from different sources.

```python
class Swimmer:
    def swim(self):
        print("I can swim.")

class Flyer:
    def fly(self):
        print("I can fly.")

class Duck(Swimmer, Flyer):
    def quack(self):
        print("Quack quack!")
```

```python
duck = Duck()
duck.swim()                   # I can swim.
duck.fly()                    # I can fly.
duck.quack()                  # Quack quack!
```

With multiple inheritance, conflicts can arise when multiple parent classes have methods with the same name. Python resolves this with the *Method Resolution Order (MRO)*, which determines the order in which classes are searched. The order corresponds to the order in which the parent classes are specified, from left to right.

```python
class A:
    def method(self):
        print("Method from A")

class B:
    def method(self):
        print("Method from B")

class C(A, B):
    pass

class D(B, A):
    pass

c = C()
c.method()                    # Method from A

d = D()
d.method()                    # Method from B
```

You can view the MRO of a class with the `mro()` method or the `__mro__` attribute.

```python
print(C.mro())
# [<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>]
```
