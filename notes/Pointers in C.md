# Pointers in C

This summary explains one of the most important and most feared ideas in the C programming language: **pointers**. A running program keeps its data in the computer's main memory (RAM). Every location in that memory has a unique number, much like a house number on a street. That number is called a **memory address**.

Many programmers avoid pointers because they seem confusing at first. That is a mistake, because pointers are a core part of C. As with any programming concept, the best way to learn them is to look at sample code and experiment with it yourself.

## Starting Point: What Is Inside a Variable?

A variable is a named storage location where a program keeps a value. Just by reading the source code, you can learn three things about a variable: its **data type** (for example `int` for whole numbers), its **name** (for example `alpha`), and the **value** assigned to it (for example `27`).

Two more properties only appear when the program runs. The first is the variable's **size**: how many bytes of memory it takes up. The **`sizeof` operator** gives you this size. The second is the variable's **address**: where in memory it is stored. You get the address with the **address-of operator `&`** (the ampersand). To print it with the `printf` function, you use the **`%p`** placeholder.

```c
#include <stdio.h>

int main(void)
{
    int alpha = 27;

    printf("Data type: int, name: alpha, value: %d\n", alpha);
    printf("Size in memory: %zu bytes\n", sizeof(alpha));
    printf("Address in memory: %p\n", &alpha);

    return 0;
}
```

On the system used in the course, an `int` variable takes up four bytes. The address shown differs from computer to computer, and often from one program run to the next. These two properties, a variable's size in memory and its address, are the foundation of pointers.

## What Is a Pointer?

**A pointer is a variable that holds a memory location.**

People often say that a pointer "points at an address." That is true, but it tends to confuse more than it helps. A pointer holds the address of another variable or of a **buffer**, which is a block of memory stored in one continuous piece. It can also hold the address of any chunk of memory the program has allocated.

Because a pointer is a variable itself, you can change what it holds, which means changing the address it stores. You can also use a pointer to read and change the data stored at that address.

## Declaring and Initializing a Pointer

You **declare** a pointer like any other variable, with a data type and a name. The difference is that the name gets an asterisk `*` in front of it. This asterisk is the **unary asterisk operator**, meaning it works on a single operand. It has nothing to do with multiplication.

Like every variable, a pointer must be **initialized**, meaning given a valid starting value, before it is used. An **uninitialized pointer** holds a random address and almost always leads to errors or crashes. To initialize a pointer, you assign it the address of another variable whose data type matches the pointer: an `int` pointer for an `int` variable, a `char` pointer for a `char` variable, and so on. The `&` operator provides that address.

```c
int alpha = 99;;
int *alphaPointer;      /* declaration: ptr is a pointer to int */

alphaPointer = &alpha;  /* initialization: ptr now holds the address of alpha */
```

## The Two "Personalities" of a Pointer

Once a pointer holds an address, you can use it in two ways.

Written **without the asterisk** (`alphaPointer`), the pointer stands for an **address** in memory. Written **with the asterisk** (`*alphaPointer`), it stands for the **data stored at that address**. Accessing the data this way is called **dereferencing** the pointer. However you use the pointer later, you always declare it with the asterisk.

## Reading and Writing Through a Pointer

The program below shows both personalities. The variable `alpha` gets the value `99`, and the pointer `alphaPointer` gets the address of `alpha`. First, the program prints the address of `alpha` and the contents of `alphaPointer`. Both values are the same because they refer to the same memory location. Next, it reads the value directly from the variable and again through the dereferenced pointer `*alphaPointer`. The `printf` statement uses `%d` for `*alphaPointer` because the value at that address is an integer.

```c
#include <stdio.h>

int main(void)
{
    int alpha;
    int *alphaPointer;

    alpha = 99;
    alphaPointer = &alpha;

    printf("Address of alpha: %p\n", &alpha);
    printf("Contents of alphaPointer:  %p\n", alphaPointer);

    printf("Value of alpha: %d\n", alpha);
    printf("Value at address %p: %d\n", alphaPointer, *alphaPointer);

    /* change the value through the pointer */
    *alphaPointer = 66;
    printf("New value of alpha: %d\n", alpha);

    return 0;
}
```

At the end, the statement `*alphaPointer = 66;` stores a new value at that memory location without touching `alpha` directly. Even so, `alpha` now holds `66`, because the pointer refers to exactly the place where `alpha` is stored.

## Pointer Math

Because a pointer holds an address, you can do arithmetic with it. This is called **pointer math** (also known as **pointer arithmetic**). The interesting question is what happens when you add 1 to a pointer used without the asterisk, that is, to the address it holds.

The answer may be surprising. The address does not go up by one byte. It goes up by the **size of the data type** the pointer refers to. On a system where integers are four bytes, an `int` pointer moves forward four bytes, which is exactly where the next integer in memory would be.

There is an important catch. If a pointer refers to a single variable, `pointer + 1` refers to an unknown chunk of memory that does not belong to the program. This is **unsafe coding practice** and should only be done to illustrate the idea. Pointer math becomes useful and safe with an **array**, which is a series of elements of the same type stored one after another in memory. In an array, `pointer + 1` refers to the next element.

```c
#include <stdio.h>

int main(void)
{
    int twos[5] = { 2, 4, 6, 8, 10 };
    int *pt;

    pt = twos;  /* no & needed: the array name stands for its base address */

    printf("Address pt:     %p\n", pt);
    printf("Address pt + 1: %p\n", (pt + 1));

    return 0;
}
```

The assignment `pt = twos;` has no address-of operator `&`. This is because of the special relationship between pointers and arrays in C. The name of an array stands for its **base address**, which is the address of its first element.

## How Large Are the Data Types?

So how far an address moves in pointer math depends on the size of the data type. You can check this for C's four standard data types with the `sizeof` operator. On the system used in the course, the results are:

1. `char` (a single character): 1 byte
2. `int` (a whole number): 4 bytes
3. `float` (a single-precision floating-point number): 4 bytes
4. `double` (a double-precision floating-point number): 8 bytes

```c
#include <stdio.h>

int main(void)
{
    char   c;
    int    i;
    float  f;
    double d;

    printf("char:   %zu byte\n",  sizeof(c));
    printf("int:    %zu bytes\n", sizeof(i));
    printf("float:  %zu bytes\n", sizeof(f));
    printf("double: %zu bytes\n", sizeof(d));

    return 0;
}
```

This means that adding 1 moves a `char` pointer forward by a single byte, an `int` pointer by four bytes, and a `double` pointer by eight bytes. These sizes can vary with the system and compiler, but the rule never changes: **adding 1 to a pointer adds the size of its data type to the address.**

## Conclusion

Pointers are variables that hold memory addresses instead of ordinary values like numbers or characters. You declare them with an asterisk and initialize them with the address-of operator `&`. You use them in two ways: without the asterisk as an address, and with the asterisk as the data stored at that address (dereferencing). A pointer lets you read and change data without using the original variable directly. Pointer math always moves an address in steps the size of the pointer's data type, which is especially useful with arrays.

If you ever lose track, remember the key sentence: **A pointer is a variable that holds a memory location.**

---

*Based on the LinkedIn Learning course "Complete Guide to C Programming Foundations" by Dan Gookin.*
