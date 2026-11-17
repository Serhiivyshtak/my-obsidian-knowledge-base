# Pointers with Arrays in C

This summary explains how **pointers** and **arrays** relate to each other in the C Programming Language. Both are basic building blocks of C, and they are closely connected. A running program keeps its data in the computer's memory, and every location in that memory has a unique number called a **memory address**.

A **[[Pointers in C|pointer]]** is a variable that holds a memory location. An **array** is a series of values of the same data type stored one after another in memory. A **string** in C is simply an array of characters. You will see why some functions need the address-of operator `&` and others don't, and how you can move through an array using only a pointer.

## Arrays Behave Like Pointers

When you read input with `scanf`, you normally put the **address-of operator `&`** in front of the variable. This passes the variable's address so that `scanf` knows where to store the input. Strings are an exception. If you read text into a character array, you leave the ampersand out.

The reason is that the compiler treats the name of an array like a pointer. The array name stands for an address: the **base address** of the array, which is the location of its first element. Since the array name is already an address, `&` isn't needed. The rule works like this. A single variable needs `&` when used with `scanf`, and so does a single array element. An array as a whole and a pointer do not.

```c
#include <stdio.h>

int main(void)
{
    char text[10];
    int number;

    printf("Enter a word: ");
    scanf("%9s", text);      /* no & needed: text is an array */

    printf("Enter a number: ");
    scanf("%d", &number);    /* & needed: number is a single variable */

    printf("You typed: %s and %d\n", text, number);

    return 0;
}
```

The format `%9s` reads no more than nine characters. That leaves room in the ten-element array for the **null character** that ends every string, which is explained later in this summary.

To show that the array name really is an address, you can assign it to a pointer and print both. Again, the assignment needs no `&`. The two printed addresses are identical.

```c
#include <stdio.h>

int main(void)
{
    char text[10];
    char *p;

    p = text;   /* no & needed: the array name is already an address */

    printf("Address of text: %p\n", text);
    printf("Address in p:    %p\n", p);

    return 0;
}
```

## Addresses of Individual Array Elements

Each element of an array also has its own address. In the next example, the integer array `twos` has five elements, and the pointer `pt` is set to the array's base address. A `for` loop goes through all five elements. In each pass, it prints two addresses: the address `pt + x`, calculated with the pointer, and the address of the element `twos[x]`, taken with the `&` operator.

This works because of **pointer math** (also called **pointer arithmetic**). Adding a number to a pointer does not move the address by that many bytes. Instead, it moves the address by that many *elements*, so each step is the size of the pointer's data type. `pt + 1` therefore points exactly to the next integer in the array. A single array element is an individual variable, so it needs the `&` operator. The output shows that both addresses are identical in every pass of the loop.

```c
#include <stdio.h>

int main(void)
{
    int twos[5] = { 2, 4, 6, 8, 10 };
    int *pt;
    int x;

    pt = twos;

    for (x = 0; x < 5; x++) {
        printf("Element %d: %p  %p\n", x, (void *)(pt + x), (void *)&twos[x]);
    }

    return 0;
}
```

## Array Notation and Pointer Notation

You can reach the values in an array in two ways. **Array notation** uses square brackets, as in `twos[2]`. **Pointer notation** uses the asterisk operator together with an address, as in `*(pt + 2)`. The asterisk performs **dereferencing**: it fetches the value stored at an address instead of the address itself.

In pointer notation, the expression inside the parentheses works out the address first: the base address of the array plus an offset. Then the asterisk fetches the value stored there. For the first element, the offset is zero. Writing `*(pt + 0)` isn't strictly necessary, since `*pt` gives the same result, but it shows the pattern used for the other elements.

```c
#include <stdio.h>

int main(void)
{
    int twos[5] = { 2, 4, 6, 8, 10 };
    int *pt;

    pt = twos;

    /* array notation */
    printf("%d %d %d %d %d\n", twos[0], twos[1], twos[2], twos[3], twos[4]);

    /* pointer notation: same output */
    printf("%d %d %d %d %d\n", *(pt + 0), *(pt + 1), *(pt + 2), *(pt + 3), *(pt + 4));

    return 0;
}
```

## Why the Parentheses Matter

The parentheses in pointer notation are required. If you leave them out, the expression means something completely different. In C, the asterisk operator is applied before addition. So `*pt + 1` first fetches the value at address `pt` and then adds 1 to that value. It does not move to the next element.

In the example array, the first element is `2`. The expression `*(pt + 1)` gives `4`, the value of the second element, which is what you want. The expression `*pt + 1` gives `3`, the value of the first element plus one. This looks a bit odd at first, but it follows directly from how C evaluates expressions.

```c
int twos[5] = { 2, 4, 6, 8, 10 };
int *pt = twos;

printf("%d\n", *(pt + 1));  /* prints 4: the value at address pt + 1 */
printf("%d\n", *pt + 1);    /* prints 3: the value at pt, plus 1 */
```

## Summary of the Relationship

The relationship between pointers and arrays comes down to a few rules. The base of an array acts like a pointer, and the pointer and the array must have the same data type. Under these conditions, element `n` of the array is the same as the value at the pointer's address plus `n`. In code, `array[n]` matches `*(pointer + n)`.

To work through an array with a pointer, you follow these steps:

1. Initialize the pointer to the array. Every pointer must be initialized before it is used.
2. Use the asterisk operator to access the current element.
3. Increment the pointer variable to move to the next element.
4. Repeat these steps until you have processed the whole array.

Even so, it's important to understand that pointers and arrays are **two separate things** in C. *A pointer is not an array, and an array is not a pointer.* For example, an array has a fixed size, while the memory a pointer refers to can be allocated and resized as the program runs. Array notation is also not a way to avoid learning pointers. Anyone learning C should learn and understand how pointers work.

## Printing a String Through a Pointer

Lets assume we want to iterate through a string using pointers.

One fact is key to solving this. Every string in C, including a **string literal** (text written directly in double quotes), automatically ends with the **null character** `\0`. This invisible character marks the end of the string. A loop can watch for it to know when to stop. The pointer also has to change somehow during the loop so that it moves through the string.

### Solution 1: Moving the Pointer

The first solution creates a character pointer `t`, which matches the array's data type: `char` for `char`. The pointer is set to the array `title`. No `&` is needed because `title` is an array, and no asterisk is used because the line assigns an address, not a value.

A `while` loop is a good fit for checking for the null character. The expression `*t` dereferences the pointer, meaning it gives the character stored at the address in `t`. The loop runs as long as that character isn't `\0`. Inside the loop, `putchar(*t)` prints the current character, and `t++` moves the pointer to the next character.

```c
#include <stdio.h>

int main(void)
{
    char title[] = "Pointers don't intimidate me.";
    char *t;

    t = title;

    while (*t != '\0') {
        putchar(*t);
        t++;
    }

    putchar('\n');

    return 0;
}
```

### Solution 2: Keeping the Pointer Unchanged

The first solution has a drawback. After the loop, `t` no longer holds the start of the string. It now points to the null character at the end. In real programs, you often need to keep the original address in a pointer so you can use it again later.

The bonus solution leaves the pointer alone and uses a second variable, the integer `x`, as an **offset**. `x` must be set to `0` before the loop starts. The program then works out each character's address as `t + x`, and the asterisk fetches the value at that address with `*(t + x)`. Only `x` is increased in each pass, while `t` keeps pointing to the start of the string. The output is exactly the same.

```c
#include <stdio.h>

int main(void)
{
    char title[] = "Pointers don't intimidate me.";
    char *t;
    int x;

    t = title;
    x = 0;

    while (*(t + x) != '\0') {
        putchar(*(t + x));
        x++;
    }
    putchar('\n');

    /* t still holds the start of the string and can be reused */

    return 0;
}
```

## Conclusion

In C, the name of an array acts like a pointer to its first element. That is why arrays and pointers need no `&` operator in `scanf` or when a pointer is assigned to an array, while single variables and single array elements do. Thanks to pointer math, `array[n]` and `*(pointer + n)` refer to the same element. The parentheses in pointer notation are required, because `*pointer + n` adds to the value instead of moving the address.

To work through a string with a pointer, you can either move the pointer itself or keep it unchanged and use a separate offset variable. Keeping the original address is often the better choice, because the pointer can then be used again elsewhere in the program. Even though they are closely related, pointers and arrays remain two separate concepts.

---

*Based on the LinkedIn Learning course "Complete Guide to C Programming Foundations" by Dan Gookin.*
