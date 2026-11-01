# Python Lists

## What Are Lists in Python?

Python does not have a built-in array type in the traditional sense found in languages like C or Java. Instead, Python provides *lists*, which serve the same purpose but are more flexible and powerful. A *list* is an ordered collection of items that can store multiple values in a single variable.

Lists in Python are *dynamic*, meaning they can grow or shrink in size as needed. They are also *heterogeneous*, allowing you to store values of different types in the same list, though it is common practice to store items of the same type for consistency and clarity.

## Creating Lists

You create a list by placing values inside square brackets, separated by commas. An empty list is created using empty square brackets or the `list()` function.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty_list = []
another_empty = list()
```

You can also create lists from other sequences using the `list()` function, or generate lists with repeated values using the multiplication operator.

```python
letters = list("Python")           # ['P', 'y', 't', 'h', 'o', 'n']
zeros = [0] * 5                    # [0, 0, 0, 0, 0]
pattern = [1, 2] * 3               # [1, 2, 1, 2, 1, 2]
```

## Accessing Elements

Lists are *zero-indexed*, meaning the first element is at position 0, the second at position 1, and so on. You access individual elements using square brackets with the index number.

```python
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])      # apple
print(fruits[1])      # banana
print(fruits[2])      # cherry
```

*Negative indexing* allows you to access elements from the end of the list. The index `-1` refers to the last element, `-2` to the second-to-last, and so on.

```python
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[-1])     # date
print(fruits[-2])     # cherry
print(fruits[-3])     # banana
```

Attempting to access an index that does not exist raises an *IndexError*.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[10])     # IndexError: list index out of range
```

## Slicing

*Slicing* allows you to extract a portion of a list, creating a new list containing the selected elements. The syntax is `list[start:stop]`, where `start` is the index where the slice begins (inclusive) and `stop` is where it ends (exclusive).

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])   # [2, 3, 4]
print(numbers[0:3])   # [0, 1, 2]
print(numbers[5:8])   # [5, 6, 7]
```

You can omit the start or stop values to slice from the beginning or to the end of the list.

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[:4])    # [0, 1, 2, 3]
print(numbers[6:])    # [6, 7, 8, 9]
print(numbers[:])     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (creates a copy)
```

A third parameter called *step* allows you to skip elements. The syntax is `list[start:stop:step]`.

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[::2])   # [0, 2, 4, 6, 8] (every second element)
print(numbers[1::2])  # [1, 3, 5, 7, 9] (every second element starting from index 1)
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed list)
```

## Modifying Elements

Lists are *mutable*, meaning you can change their contents after creation. You modify an element by assigning a new value to a specific index.

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)         # ['apple', 'blueberry', 'cherry']
```

You can also replace a range of elements using slicing.

```python
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [20, 30, 40]
print(numbers)        # [1, 20, 30, 40, 5]

numbers[1:3] = [200]
print(numbers)        # [1, 200, 40, 5]
```

## Adding Elements

There are several ways to add new elements to a list.

The `append()` method adds a single element to the end of the list.

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)         # ['apple', 'banana', 'cherry']
```

The `insert()` method adds an element at a specific position. The first argument is the index where the element should be inserted.

```python
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")
print(fruits)         # ['apple', 'banana', 'cherry']
```

The `extend()` method adds all elements from another list (or any iterable) to the end of the current list.

```python
fruits = ["apple", "banana"]
more_fruits = ["cherry", "date"]
fruits.extend(more_fruits)
print(fruits)         # ['apple', 'banana', 'cherry', 'date']
```

You can also concatenate lists using the `+` operator, which creates a new list without modifying the originals.

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)       # [1, 2, 3, 4, 5, 6]
```

## Removing Elements

The `remove()` method removes the first occurrence of a specified value. If the value is not found, it raises a *ValueError*.

```python
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)         # ['apple', 'cherry', 'banana']
```

The `pop()` method removes and returns an element at a specified index. If no index is provided, it removes and returns the last element.

```python
fruits = ["apple", "banana", "cherry"]
last = fruits.pop()
print(last)           # cherry
print(fruits)         # ['apple', 'banana']

first = fruits.pop(0)
print(first)          # apple
print(fruits)         # ['banana']
```

The `del` statement removes an element at a specific index or deletes a slice of elements.

```python
numbers = [0, 1, 2, 3, 4, 5]
del numbers[2]
print(numbers)        # [0, 1, 3, 4, 5]

del numbers[1:3]
print(numbers)        # [0, 4, 5]
```

The `clear()` method removes all elements from a list, leaving it empty.

```python
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)         # []
```

## Searching and Counting

The `in` operator checks whether a value exists in a list, returning `True` or `False`.

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)     # True
print("grape" in fruits)      # False
print("grape" not in fruits)  # True
```

The `index()` method returns the index of the first occurrence of a specified value. If the value is not found, it raises a *ValueError*.

```python
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.index("banana"))     # 1
print(fruits.index("cherry"))     # 2
```

The `count()` method returns the number of times a specified value appears in the list.

```python
numbers = [1, 2, 2, 3, 2, 4, 2]
print(numbers.count(2))       # 4
print(numbers.count(5))       # 0
```

## Sorting and Reversing

The `sort()` method sorts the list in place, modifying the original list. By default, it sorts in ascending order.

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)        # [1, 1, 2, 3, 4, 5, 6, 9]
```

To sort in descending order, use the `reverse=True` parameter.

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort(reverse=True)
print(numbers)        # [9, 6, 5, 4, 3, 2, 1, 1]
```

The `sorted()` function returns a new sorted list without modifying the original.

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers) # [1, 1, 2, 3, 4, 5, 6, 9]
print(numbers)        # [3, 1, 4, 1, 5, 9, 2, 6] (unchanged)
```

The `reverse()` method reverses the list in place.

```python
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)         # ['cherry', 'banana', 'apple']
```

## List Length and Other Functions

The `len()` function returns the number of elements in a list.

```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))    # 3
```

The `min()` and `max()` functions return the smallest and largest values in a list.

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(min(numbers))   # 1
print(max(numbers))   # 9
```

The `sum()` function returns the total of all numeric values in a list.

```python
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))   # 15
```

## Copying Lists

Assigning a list to a new variable does not create a copy. Both variables will reference the same list in memory, so changes to one will affect the other.

```python
original = [1, 2, 3]
reference = original
reference[0] = 100
print(original)       # [100, 2, 3]
```

To create an independent copy, use the `copy()` method, slicing, or the `list()` function.

```python
original = [1, 2, 3]
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

copy1[0] = 100
print(original)       # [1, 2, 3] (unchanged)
print(copy1)          # [100, 2, 3]
```

For lists containing other lists (nested lists), these methods create a *shallow copy*, meaning the inner lists are still references. Use the `deepcopy()` function from the `copy` module for a complete independent copy.

```python
import copy

original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)

shallow[0][0] = 100
print(original)       # [[100, 2], [3, 4]] (affected by shallow copy change)

deep[1][1] = 400
print(original)       # [[100, 2], [3, 4]] (not affected by deep copy change)
```

## Nested Lists (Multi-Dimensional Arrays)

A *nested list* is a list that contains other lists as elements. This allows you to create structures similar to multi-dimensional arrays or matrices.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

You access elements in nested lists using multiple index brackets. The first index selects the inner list, and the second index selects the element within that inner list.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])      # [1, 2, 3]
print(matrix[0][1])   # 2
print(matrix[2][2])   # 9
```

You can iterate through nested lists using nested loops.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

## List Comprehensions

A *list comprehension* is a concise way to create lists based on existing lists or other iterables. It combines a loop and an optional condition into a single line.

The basic syntax is `[expression for item in iterable]`.

```python
squares = [x ** 2 for x in range(1, 6)]
print(squares)        # [1, 4, 9, 16, 25]

doubled = [x * 2 for x in [1, 2, 3, 4, 5]]
print(doubled)        # [2, 4, 6, 8, 10]
```

You can add a condition to filter which elements are included.

```python
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)   # [0, 2, 4, 6, 8]

positive = [x for x in [-2, -1, 0, 1, 2, 3] if x > 0]
print(positive)       # [1, 2, 3]
```

List comprehensions can also work with strings and nested loops.

```python
uppercase = [char.upper() for char in "hello"]
print(uppercase)      # ['H', 'E', 'L', 'L', 'O']

pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)          # [(1, 3), (1, 4), (2, 3), (2, 4)]
```
