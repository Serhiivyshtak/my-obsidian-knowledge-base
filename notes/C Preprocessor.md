# C Preprocessor

This summary explains two related topics in the [[C Programming Language]]. The first is the **preprocessor**, a program that edits the source code before the actual translation begins. The second is the difference between **header files** and **libraries**.

To understand both, it helps to look briefly at how C source code becomes a program you can run. C is a **compiled language**. The **source code** (the text a person writes) is translated in several steps into **machine code**, which is made of instructions the processor can run directly. Put simply, three stages run one after another. First, the **preprocessor** prepares the source code. Next, the **compiler** translates the prepared code into **object code**, which is binary machine code. Finally, the **linker** combines this object code with the libraries it needs to produce a finished, executable program.

## What Is the Preprocessor?

The **preprocessor** is the first stage in translating a C program. It reads the source file, changes its text according to certain instructions and passes the result, called the **preprocessed file**, on to the compiler. So the compiler never sees the original source code. It only sees the version the preprocessor has edited.

The preprocessor has three main tasks. It **expands macros**, meaning it replaces defined names with the text assigned to them. It **inserts header files** by copying their contents into the source code. And it evaluates **conditional directives**, so that certain sections of code are kept or removed depending on a condition.

The preprocessor is controlled by **preprocessor directives**. These are special instructions that always begin with the hash sign `#`, such as `#include` or `#define`. Unlike ordinary C statements, they **do not end with a semicolon**. The most important directives include `#define`, `#undef`, `#include`, `#if`, `#ifdef`, `#ifndef`, `#elif`, `#else`, `#endif`, `#pragma`, `#error` and `#line`.

If you want to see what the preprocessor does to a file, the GCC and Clang compilers can show you the result of this first stage with the `-E` option, without compiling the program:

```bash
gcc -E program.c
```

## Macros

A **macro** is a name that has a replacement text assigned to it. Wherever the name appears in the source code, the preprocessor inserts the replacement text before compilation. In other words, it is pure **text replacement**. You define macros with the **`#define`** directive. With **`#undef`**, you remove a macro that was defined earlier.

```c
#define NAME replacement_text
#undef NAME
```

Here, `NAME` is the **macro name**, and `replacement_text` is the value or expression that takes its place. Macro names are usually written in capital letters so they are easy to tell apart from variables in the code. A typical use is defining **constants**, which are fixed values needed in many places in a program:

```c
#include <stdio.h>

#define LIMIT 5

int main(void) {
    for (int i = 0; i < LIMIT; i++) {
        printf("%d\n", i);
    }

    return 0;
}
```

Before compilation, the preprocessor replaces every occurrence of `LIMIT` with `5`. The compiler therefore sees `i < 5`, and the program prints the numbers 0 through 4. If the limit needs to change later, you only have to edit one place.

Once a macro is removed with `#undef`, no more replacement happens from that point on. In the following example, `LIMIT` stays in the code unchanged. The compiler doesn't know any variable with that name and reports an error such as *"'LIMIT' undeclared"*:

```c
#include <stdio.h>

#define LIMIT 5
#undef LIMIT

int main(void) {
    /* error: LIMIT is no longer defined */
    for (int i = 0; i < LIMIT; i++) {
        printf("%d\n", i);
    }

    return 0;
}
```

Besides macros you define yourself, C also provides **predefined macros** that supply useful information during translation. `__FILE__` holds the name of the current source file, `__LINE__` the current line number, `__DATE__` the date and `__TIME__` the time of translation. They are especially helpful for debugging:

```c
#include <stdio.h>

int main(void) {
    printf("File: %s, line: %d\n", __FILE__, __LINE__);
    printf("Compiled on %s at %s\n", __DATE__, __TIME__);
    return 0;
}
```

## Macros With Arguments

Macros can also take **parameters**. These **function-like macros** look like function calls, but the preprocessor resolves them through text replacement. As a result, there is no cost for a real function call, which used to be an important advantage in performance-critical code.

```c
#define MACRO_NAME(arg1, arg2) replacement_text
```

Important: there must be **no space** between the macro name and the opening parenthesis. Otherwise, the preprocessor treats the parenthesis as part of the replacement text. The following example calculates the area of a rectangle:

```c
#include <stdio.h>

#define AREA(l, b) ((l) * (b))

int main(void) {
    int a = 10, b = 5;

    printf("%d\n", AREA(a, b));   /* output: 50 */

    return 0;
}
```

The preprocessor replaces `AREA(a, b)` with `((a) * (b))`. The actual multiplication only happens at runtime, because the values of `a` and `b` are not yet known during translation.

All the parentheses in the replacement text are there for a reason. Because a macro is pure text replacement, leaving out parentheses can lead to surprising results. In C, multiplication is done before addition. Without parentheses around the parameters, `AREA(2 + 3, 4)` would expand to `2 + 3 * 4`, giving `14` instead of `20`:

```c
#define AREA_WRONG(l, b) (l * b)
#define AREA_RIGHT(l, b) ((l) * (b))

/* AREA_WRONG(2 + 3, 4) becomes (2 + 3 * 4)       = 14 */
/* AREA_RIGHT(2 + 3, 4) becomes ((2 + 3) * (4))   = 20 */
```

As a rule of thumb, put **every parameter and the entire replacement text in parentheses**.

## Including Files With #include

The **`#include`** directive inserts the contents of another file into the source code at exactly that spot. Usually this is a **header file** (with the extension `.h`) that contains declarations of functions, constants and data types. This makes it possible to reuse code and split a program into manageable modules.

There are two ways to write it, and they differ in where the preprocessor looks for the file:

```c
#include <stdio.h>     /* searches the system's standard directories */
#include "my.h"        /* searches the source file's directory first */
```

With **angle brackets** `< >`, the preprocessor searches the system's **standard directories**, where the header files of the standard library are kept. With **double quotes** `" "`, it first searches the **directory of the current source file** and only then the standard directories. So you use angle brackets for system and standard headers, and double quotes for your own header files.

```c
#include <stdio.h>   /* includes standard input/output */

int main(void) {
    printf("Hello World\n");
    return 0;
}
```

## Conditional Compilation

With **conditional compilation**, you decide that certain parts of a program are only translated if a condition is met. The preprocessor removes code sections whose condition is false completely, so the compiler never sees them. Typical uses are **platform-specific code** (for example, different code for Windows and Linux), extra **debug output** during development, and **optional features** that can be switched on and off.

Several directives are available for this. **`#if`** checks a constant expression, **`#ifdef`** checks whether a macro is defined, and **`#ifndef`** checks whether a macro is *not* defined. **`#elif`** ("else if") checks another condition, **`#else`** applies when no earlier condition was true, and **`#endif`** closes every block started with `#if`, `#ifdef` or `#ifndef`.

```c
#include <stdio.h>

#define PI 3.14159

int main(void) {
#ifdef PI
    printf("PI is defined\n");
#elif defined(SQUARE)
    printf("SQUARE is defined\n");
#else
    #error "Neither PI nor SQUARE is defined"
#endif

#ifndef SQUARE
    printf("SQUARE is not defined\n");
#else
    printf("SQUARE is defined\n");
#endif

    return 0;
}
```

Because `PI` is defined, only the first output line of the first block is kept. The expression `defined(SQUARE)` is how you check, inside `#if` or `#elif`, whether a macro exists. The second block uses `#ifndef` to check whether `SQUARE` is *not* defined. That is true, so the output is:

```text
PI is defined
SQUARE is not defined
```

A very common use of `#ifndef` is the **include guard**. It prevents the contents of a header file from being inserted more than once when the file is included several times through different paths:

```c
/* file: my.h */
#ifndef MY_H
#define MY_H

int add(int a, int b);

#endif
```

The first time the file is included, `MY_H` is not yet defined, so the contents are kept and the macro gets defined. Each time after that, `MY_H` is already known, and the preprocessor skips the entire contents.

## Other Directives

Besides macros, file inclusion and conditional compilation, C has a few more directives.

The **`#pragma`** directive passes special instructions to the compiler, for example to turn warnings on or off, to control how data is aligned in memory, or to adjust optimization. The directive itself is part of the C standard, but which pragmas exist and what they do is largely up to each compiler. A compiler usually ignores a pragma it doesn't recognize. A well-known example is `#pragma once`, which many compilers support as a shorter alternative to an include guard.

```c
#pragma once   /* supported by many compilers, but not standardized */
```

The **`#error`** directive stops translation with an error message of your choice. It is usually combined with conditional compilation to stop translation when a required condition is missing, as in the example above.

```c
#error "Error message"
```

The **`#line`** directive changes the line number, and optionally the file name, that the compiler reports in its messages. It is mainly used by **code generators**, which are programs that produce C code automatically. This way, error messages refer to the original input file instead of the generated code.

```c
#line 100 "original.c"
```

## Header Files and Libraries: Two Different Things

Beginners often confuse **header files** with **libraries**. The two belong together, but they are fundamentally different. In short, header files are used in the **source code** and included by the preprocessor, while libraries are used by the **linker**.

A **header file** contains ordinary C code: mainly **function prototypes** (declarations that tell the compiler a function's name, parameters and return type), plus constants, data types and preprocessor directives. It usually does not contain the actual code of the functions, meaning the statements that run when a function is called. On Unix systems such as Linux, header files are traditionally kept in the **`/usr/include`** directory. The preprocessor fetches them from there when you use `#include` with angle brackets.

A **library**, on the other hand, contains already translated **object code**: binary data of exactly the kind the compiler produces, not readable C code. Libraries are traditionally kept in the **`/usr/lib`** directory. When a program is built, the linker looks there for the libraries it needs to link in. The most important one is the **C standard library**, which contains the code for functions such as `printf`. Other locations are used as well, but these two directories are the traditional ones.

You can picture the division of labor like this. The header file is like an instruction manual that tells the compiler how to call a function. The library provides the actual "muscle," the code that does the work. It's no accident that functions such as `printf` or `sqrt` are called **library functions**.

When something is missing, it shows up in different ways. If the right header file is missing, the **compiler** gives a warning, or an error with newer compilers and standards, because it doesn't know the function. If the library is missing or the function name is misspelled, the **linker** reports an error, because it can't find the function's code.

## Documentation Through Man Pages

A function's documentation tells you which header file and which library it needs. On Unix systems, this documentation comes as **man pages** (short for *manual pages*), which you open in the terminal with the `man` command followed by the function name. Copies are also available online.

```bash
man sqrt
```

The man page for the square root function `sqrt` shows that the header file `math.h` must be included and describes the different forms of the function. On some platforms, such as Linux with GCC, it also notes that the **math library** must be named explicitly when linking. Press `Q` to quit the `man` program.

## Example: The Math Library

The following program shows how a header file and a library work together. It calculates a sine with the `sin` function and uses the constant `M_PI` for the number pi:

```c
#include <stdio.h>
#include <math.h>   /* provides the declaration of sin() and the constant M_PI */

int main(void)
{
    double angle = M_PI / 2.0;

    printf("sin(pi/2) = %f\n", sin(angle));   /* output: 1.000000 */
    return 0;
}
```

The header file `math.h` provides the declaration of the `sin` function and the definition of `M_PI`. Note that `M_PI` is not part of the C standard itself but of the Unix standard **POSIX**, so on some systems it is only available with extra settings. The actual code of the sine function lives in the math library, and this library must be linked in when the program is built. The header file alone can't do that. On Linux with GCC, you name the library with the `-lm` option:

```bash
gcc program.c -o program -lm
```

The `-l` tells the linker to link in a library, and `m` is the short name of the math library. Without this option, depending on the system, the linker may not find the `sin` function and stops with an error such as *"undefined reference to sin"*.

## Key Points at a Glance

1. The preprocessor edits the source code **before** compilation and passes the result to the compiler.
2. Preprocessor directives begin with `#` and do **not** end with a semicolon.
3. Macros are pure text replacement, so parameters and the replacement text belong in parentheses.
4. Header files contain C code with declarations and are included by the preprocessor. Libraries contain object code and are linked in by the linker.

## Conclusion

The preprocessor is the first stage in translating a C program. You use `#define` to define constants and function-like macros, `#include` to include header files, and `#if`, `#ifdef` and `#ifndef` to control which parts of the code are translated. Additional directives such as `#pragma`, `#error` and `#line` control the compiler's behavior and its messages.

The difference between header files and libraries matters just as much. A header file tells the compiler *how* a function is called. The library provides the code that actually carries out the function. A working program needs both: the right `#include` line in the source code and, where necessary, the matching library at link time. A function's documentation, such as its man page, tells you which ones you need.

---

*Sources:*

- *LinkedIn Learning course "Complete Guide to C Programming Foundations" by Dan Gookin*
- *[C Preprocessors](https://www.geeksforgeeks.org/c/cc-preprocessors/)*
