# `typedef` Keyword in C

In [[C Programming Language|C]], every value has a **data type**, such as `int` for whole numbers or `char` for characters. Some type names are long or hard to read, especially for structures, pointers, and function pointers. The **`typedef`** keyword lets you give an existing type a second, shorter, or more meaningful name.

## What `typedef` Does

A **`typedef`** creates an ***alias***, which is an extra name for an existing data type. It does **not** create a new type. After the declaration, the alias and the original type can be used interchangeably, and the compiler treats them as the same type. The main benefits are readability and easier maintenance: if the underlying type changes, you only edit one line.

The syntax is `typedef existing_type new_name;`.

```c
#include <stdio.h>

typedef int Integer;
typedef long long ll;

int main(void) {
    Integer n = 10;   /* same as: int n = 10; */
    ll big = 20;      /* same as: long long big = 20; */

    printf("%d %lld\n", n, big);
    return 0;
}
```

**Naming convention:** the C standard library and POSIX (a standard for Unix-like systems) often end type aliases with ***`_t`***, as in `size_t` and `time_t`. POSIX reserves this suffix for its own types, so it is safer not to use it for your own aliases.

## Aliases as Documentation

A `typedef` can tell the reader what a value means, not only how it is stored. In the example below, both aliases are plain `int`, but the names show what each parameter should contain.

```c
typedef int KmPerHour;
typedef int Points;

void congratulate(Points score, KmPerHour top_speed);
```

This is **only a hint for humans**. The compiler replaces each alias with its underlying type before it checks for errors, so swapping the two arguments compiles without any warning.

## Structures, Unions, and Enums

A ***structure*** (`struct`) groups several related values under one name. In C, you normally have to repeat the `struct` keyword every time you declare a variable of that type. A `typedef` removes this repetition. The same applies to ***unions*** (`union`), which store different types in the same memory, and ***enumerations*** (`enum`), which are sets of named integer constants.

You can define the type and its alias in a single statement. The ***tag***, which is the name after `struct` or `enum`, is optional in that case. If you leave it out, only the alias exists.

```c
#include <stdio.h>
#include <string.h>

typedef struct Student {
    char name[50];
    int id;
} Student;

typedef enum {
    CLOUDY,
    RAINY,
    SUNNY
} Weather;

int main(void) {
    Student s; /* instead of: struct Student s; */
    Weather today = SUNNY;

    strcpy(s.name, "Geeks");
    s.id = 108;

    printf("%s %d %d\n", s.name, s.id, today);
    return 0;
}
```

## Pointers

A ***pointer*** is a variable that stores the memory address of another value. A `typedef` can name a pointer type:

```c
typedef int *IntPtr;

IntPtr a, b; /* both a and b are int* */
IntPtr c, *d; /* c is int*, but d is int** (pointer to pointer) */
```

This works because a `typedef` defines a real type and is **not a text substitution**. In a plain declaration such as `int *a, b;`, only `a` is a pointer and `b` is an ordinary `int`, which is a common typo. With the alias, every variable in the list is a pointer:

```c
typedef struct Node *NodePtr;

NodePtr start, end, current; /* all three are struct Node* */
```

**`const` pitfall:** for the same reason, `const IntPtr p` makes the ***pointer itself*** constant (`int *const p`). It does **not** make the integer it points to constant. Because the pointer can't be changed later, it must be given its value when it is declared.

```c
typedef int *IntPtr;

int value = 5;
const IntPtr p = &value;   /* equivalent to: int *const p = &value; */
```

## Function Pointers

A ***function pointer*** stores the address of a function, so the function can be passed around and called later. Function pointer syntax is hard to read, and `typedef` helps the most here.

```c
typedef int (*MathFunc)(float, int);

int do_math(float a, int b) {
    return b;
}

int call_a_func(MathFunc f) {
    return f(5.5f, 7);
}

int result_example(void) {
    return call_a_func(do_math);
}
```

`MathFunc` is a pointer to a function that takes a `float` and an `int` and returns an `int`. The difference is even larger for functions that return function pointers, such as the standard `signal` function:

```c
/* Without typedef */
void (*signal(int sig, void (*func)(int)))(int);

/* With typedef */
typedef void (*sighandler_t)(int);
sighandler_t signal(int sig, sighandler_t func);
```

## Arrays

A `typedef` can also name an array type with a fixed size:

```c
typedef int Arr4[4];

Arr4 a = {10, 20, 30, 40};   /* same as: int a[4] = {10, 20, 30, 40}; */
Arr4 *pa = &a;               /* pointer to an array of 4 ints */
```

## Type Casts

A ***type cast*** converts a value to a different type. Without `typedef`, the syntax for declaring a complex type is different from the syntax for casting to it. With an alias, the same name works in both places:

```c
#include <stddef.h>

typedef int (*FuncPtr)(double);

void *p = NULL;
FuncPtr x = (FuncPtr)p;   /* alias used for both declaration and cast */
```

---

*Sources:*

- *LinkedIn Learning course "Complete Guide to C Programming Foundations" by Dan Gookin*
- *Wikipedia article [typedef](https://en.wikipedia.org/wiki/Typedef)*
- *Geeksforgeeks article [C typedef](https://www.geeksforgeeks.org/c/typedef-in-c/)*
