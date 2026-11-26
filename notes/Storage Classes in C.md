# Storage Classes in C

In C, every [[Variables & Datatypes in C|variable]] has a **storage class**. It controls two things. The first is **scope**, which is where in the code the variable can be used. The second is **lifetime**, which is how long the variable and its value exist while the program runs. You choose the storage class with a keyword in front of the declaration. C has four of them: `auto`, `static`, `register` and `extern`.

| Storage class | Scope | Lifetime | Default value |
| --- | --- | --- | --- |
| `auto` | Local (block or function) | Until the block ends | Undefined (garbage) |
| `static` | Local (block or function) | Entire program run | Zero |
| `register` | Local (block or function) | Until the block ends | Undefined (garbage) |
| `extern` | Global (all functions, even in other files) | Entire program run | Zero |

## auto: The Default

An **auto variable** is local, or private, to the function or block where it is declared. It is created when the function starts and discarded when the function returns. If you don't initialize it, it holds a random leftover value, often called a **garbage value**. Every variable declared inside a function is `auto` by default, so you almost never write the keyword.

```c
#include <stdio.h>

int sum(void) {
    auto int a = 5;   /* same as: int a = 5; */
    int b = 10;       /* also auto by default */
    return a + b;     /* a and b are discarded after this */
}

int main(void) {
    printf("%d\n", sum());   /* output: 15 */
    return 0;
}
```

Since the C23 standard, `auto` has a second meaning. Similar to C++, it can let the compiler work out a variable's type, as in `auto x = 10;`.

## static: Local but Persistent

A **static variable** declared inside a function is still local, so no other function can see it. However, it keeps its value after the function returns. It is initialized only once, and to zero if you give no value. The next time the function is called, the variable continues from its last value.

```c
#include <stdio.h>

void counter(void) {
    static int count = 0;   /* initialized only once */
    count++;
    printf("Count = %d\n", count);
}

int main(void) {
    counter();   /* Count = 1 */
    counter();   /* Count = 2 */
    return 0;
}
```

A common use is returning a string from a function. An auto array is destroyed when the function returns, so the caller receives the address of memory that no longer exists. Using it leads to **undefined behavior**: the program may print nonsense, print `(null)` or crash. The compiler usually warns about this. Making the array `static` fixes the problem, because its memory stays valid for the whole program.

```c
#include <stdio.h>

char *myname(void) {
    /* WRONG: char me[] = "Dan Gookin";  (destroyed on return) */
    static char me[] = "Dan Gookin";   /* RIGHT: survives the return */
    return me;
}

int main(void) {
    printf("The course's author is %s\n", myname());
    return 0;
}
```

When `static` is used outside of any function, it means something different. The variable then exists for the whole program but is visible only inside its own source file.

## register: A Speed Hint

A **register variable** works like an auto variable. The only difference is that it asks the compiler to keep the variable in a **CPU register**, a very small and very fast storage location inside the processor, rather than in main memory. This is only a suggestion, and modern compilers usually ignore it because they optimize better on their own. A register variable has one restriction: you cannot take its address with the `&` operator.

```c
#include <stdio.h>

int main(void)
{
    register int i;   /* request: keep i in a CPU register */

    for (i = 0; i < 5; i++)
    {
        printf("%d ", i);   /* output: 0 1 2 3 4 */
    }
    return 0;
}
```

## extern: Global Variables

An **external variable**, also called a **global variable**, is defined outside of every function. It exists for the entire program run, and all functions can use it. Inside a function, the `extern` keyword tells the compiler that the variable is defined somewhere else, outside the function, and that it should look for it there. This marks the difference between a **definition**, which creates the variable and reserves memory, and a **declaration**, which only announces that the variable exists. Every function that uses the variable works with the same single copy.

```c
#include <stdio.h>

int a, b;   /* definition: outside all functions */

void twice(void) {
    extern int a, b;   /* optional here: a and b are defined above */
    a *= 2;
    b *= 2;
}

int main(void) {
    extern int a, b;
    a = 5;
    b = 10;
    twice();
    printf("a = %d, b = %d\n", a, b);   /* output: a = 10, b = 20 */
    return 0;
}
```

In a single file, `extern` inside a function is optional, because a variable defined above is already visible. The keyword becomes essential when a program is split across several files. The variable must be **defined exactly once** in one file and **declared with `extern`** in every other file that uses it. Both files are then compiled together.

```c
/* file: printvar.c */
#include <stdio.h>

int globalVar = 100;   /* definition: memory is reserved here */

void printGlobalVar(void) {
    printf("Global variable is: %d\n", globalVar);
}
```

```c
/* file: main.c */
extern int globalVar;        /* declaration: defined in printvar.c */
void printGlobalVar(void);

int main(void) {
    globalVar = 200;
    printGlobalVar();   /* output: Global variable is: 200 */
    return 0;
}
```

## When to Use External Variables

It is tempting to make every variable global, and some other languages encourage this. In C, it is considered sloppy and inefficient. Any function can change a global variable, which makes errors hard to trace. Use external variables only when they really must be shared by all functions, or when passing them around would be much too complicated. In most cases, the better solution is to pass values to functions as **arguments** and get results back as **return values**.

## Conclusion

Storage classes determine where a variable can be used and how long it lives. `auto` is the default for local variables, which disappear when their function ends. `static` keeps a local variable's value between calls. `register` is an outdated speed hint. `extern` declares a global variable that is defined elsewhere, possibly in another file. Keep variables as local as possible, and use global variables only when there is no reasonable alternative.

---

*Sources:*

- *LinkedIn Learning course "Complete Guide to C Programming Foundations" by Dan Gookin*
- *[Storage Classes in C](https://www.geeksforgeeks.org/c/storage-classes-in-c/)*
