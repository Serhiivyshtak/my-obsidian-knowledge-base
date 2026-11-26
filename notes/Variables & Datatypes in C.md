# Variables & Datatypes in C

Every program works the same way at its core: it receives **input**, changes it, and produces **output** (often shortened to *I/O*). To work with data, a [[C Programming Language|C]] program has to know what kind of data it is handling and where to keep it. This is the job of **data types**, **variables**, and **constants**.

## Data Types

A **data type** tells the compiler what kind of information a piece of code works with and how much memory it needs. C has four basic data types:

1. **`char`**: a single character or byte, such as `'A'`.
2. **`int`**: an *integer*, which is a whole number such as `42`.
3. **`float`**: a *real number* (decimals, fractions, very large values) in *single precision*, with about 7 significant digits.
4. **`double`**: a real number in *double precision*, with about 15 to 16 significant digits.

**Qualifiers** refine a data type. For integers, ***signed*** is the default, which means the variable can hold both positive and negative values. An ***unsigned*** integer holds only zero and positive values.

There is also the **`void`** type, which means *no type* or *undefined type*. It is used for functions that return no value or take no arguments, and when allocating memory.

The following program reads one value of each basic type and prints it back. The **`scanf()`** function reads input. Its first argument is a format string that states the expected data type, and the second argument is the *address* of the variable (marked with `&`). The **`printf()`** function prints the values.

```c
#include <stdio.h>

int main(void)
{
    char c;
    int i;
    float f;
    double d;

    printf("Enter a character, an integer, and two real numbers: ");
    scanf(" %c %d %f %lf", &c, &i, &f, &d);

    printf("char:   %c\n", c);
    printf("int:    %d\n", i);
    printf("float:  %f\n", f);
    printf("double: %f\n", d);

    return 0;
}
```

## Strings

Many languages have a text type. C does not. A **string** in C is an **array of `char` values**, which means a row of characters stored one after another. The function **`fgets()`** reads text from **`stdin`** (*standard input*, which is usually the keyboard) and stores it in the array. It never stores more characters than the array can hold.

```c
#include <stdio.h>

int main(void)
{
    char buffer[32];

    printf("Your name: ");
    fgets(buffer, 32, stdin);
    printf("Hello, %s", buffer);

    return 0;
}
```

## Variables

A **variable** is a named storage container for a value that can change. It must be **declared** before use, which means you give it a data type and a name. Variables are usually declared at the top of the function that uses them. A declaration later in the code also works, as long as it comes before the variable's first use. If you use a variable that was never declared, the compiler reports an error.

```c
char c;
int i;
float f;
```

**Naming rules:** a name must start with a letter. After that it can contain letters, numbers, and the underscore `_`. Spaces and other symbols are not allowed. Names are **case sensitive**, so `total` and `Total` are different variables. Good names are short and descriptive.

Do not use C **keywords** (such as `int` or `return`) as names. You should also avoid function names such as `puts`, and C++ keywords such as `new`. Older C standards only treat the first 31 characters of a name as significant.

**Initialization** means giving a variable its first value. You can do this when you declare it or later in the code. C does **not** set new variables to zero. An uninitialized variable holds whatever data was already in that memory, which causes unpredictable bugs and can be a security risk. **Always assign a value before you use a variable.**

```c
char c = 'A';
int i = 2;
float f = 0.25;
```

## Assignment

The **assignment operator** `=` stores a value in a variable. The variable goes on the left side and the value or expression goes on the right. The value can be a literal, a constant, another variable, a function's return value, or any C expression. Large numbers can be written in ***e-notation***, where `2.5e6` means 2.5 million.

You can declare several variables of the same type in one statement:

```c
#include <stdio.h>

int main(void)
{
    int a = 126;
    double d = 2.5e6;
    char h = 'H', e = 'e', l = 'l', o = 'o';

    printf("%d %f\n", a, d);
    printf("%c%c%c%c%c\n", h, e, l, l, o);

    return 0;
}
```

In `printf()`, **placeholders** mark where each value goes and what type it is. For example, `%c` is for a character, `%d` for an integer, and `%f` for a floating-point value.

## Constants

A **constant** is a value that never changes while the program runs. There are three kinds:

1. **Literal constants** are values written directly in the code. Examples are the number `5`, the character `'A'`, and the *string literal* `"Hello"`, which is text in double quotes.
2. **`const` declarations** create a named value that cannot be changed. It must be given its value in the same statement that declares it. The compiler reports an error if the code later tries to change it. If you declare it inside a function, you can only use it in that function.
3. **`#define` directives** are handled by the *preprocessor*, a step that runs before compilation. It replaces the name with its value everywhere in the source file, so every function in the file can use it.

```c
#include <stdio.h>

#define MAX 20

int main(void)
{
    const int count = 4;

    printf("count = %d, MAX = %d\n", count, MAX);

    return 0;
}
```

The main benefit of named constants is that each value lives in one place. If you change it there, every use of it in the code is updated, and the value can't be changed by accident.

---

*Based on the LinkedIn Learning course "Complete Guide to C Programming Foundations" by Dan Gookin*
