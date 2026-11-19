# Memory Allocation in C

This summary explains how a [[C Programming Language|C]] program can request memory while it is running, use it, resize it and give it back. This is called **dynamic memory management**. A running program keeps its data in the computer's main memory, and every location there has a unique number called a **memory address**. A **[[Pointers in C|pointer]]** is a variable that holds such a memory address.

Normally, you decide how much memory a variable uses when you write the code, for example an array with ten elements. Often, though, the right amount is only known once the program is running. A user says how many values they want to enter, a file of unknown size is loaded, or new messages keep arriving. In these cases, the program requests memory only when it needs it. A block of memory requested this way is called a **buffer**.

## Stack and Heap: Two Kinds of Memory

To understand dynamic memory management, you need to tell two memory areas apart. Ordinary local variables, meaning variables declared inside a function, live on the **stack**. The stack is managed automatically. When a function is called, space is set aside for its variables, and when the function ends, that space is released right away. This is fast and convenient, but it has two drawbacks. The stack is fairly small, only about **1 MB** by default on Windows. And the data only exists while the function is running.

Dynamically requested memory comes from the **heap** instead. The heap is much larger and, depending on the system, can hold gigabytes of data. Memory on the heap stays allocated until the program explicitly releases it or ends. This freedom comes with responsibility: the programmer has to make sure that memory is released once it is no longer needed. Unlike languages such as Java or Python, C has no **garbage collector** to do this automatically.

C provides four functions for working with the heap: `malloc()`, `calloc()`, `realloc()` and `free()`. All four are declared in the header file **`stdlib.h`**, which must therefore be included in the source code.

## Allocating Memory With malloc

The **`malloc`** function (short for *memory allocation*) reserves a contiguous block of memory on the heap. Its only argument is the number of bytes needed. This value has the data type **`size_t`**, an unsigned integer type that C provides specifically for sizes. `malloc` returns the address of the new memory block, which you store in a pointer. The program then accesses the buffer through this pointer.

The allocated memory is **not initialized**. It contains random leftover values from earlier use until the program writes its own values into it. If there isn't enough memory available, the allocation fails and `malloc` returns the constant **`NULL`**, a special address that means "no valid memory." That's why you must **compare the result with `NULL` immediately after every call**, before using the memory.

The following program allocates memory for 128 characters, checks for an error and releases the memory at the end:

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *buffer;

    buffer = malloc(sizeof(char) * 128);

    if (buffer == NULL){
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }

    puts("Buffer created");

    free(buffer);

    puts("Buffer released");

    return 0;
}
```

Instead of simply passing the number `128`, the program multiplies the number of elements it needs by the size of the data type, which the **`sizeof` operator** provides. For `char` the result is also 128 bytes, because a character takes up exactly one byte. Still, this way of writing it is a good habit, because it automatically works out the correct number of bytes for larger data types such as `int` or `double`.

If the allocation fails, the program prints an error message and ends by calling the **`exit`** function.

`malloc` returns a **`void` pointer** (`void *`), which is a pointer with no specific data type. In C, it is converted to the right pointer type automatically. An explicit type conversion such as `(int *)malloc(...)` is therefore not needed in C, unlike in C++.

## Releasing Memory With free

When the program no longer needs a buffer, it gives the memory back with the **`free`** function. Its argument is exactly the address that `malloc`, `calloc` or `realloc` returned earlier. `free` returns no value. The operating system releases all memory when the program ends anyway, but releasing every allocated block yourself is **good programming practice**. For programs that run for a long time, such as servers or background services, it is essential.

After calling `free`, the pointer is **invalid**. It still holds the old address, but the memory there no longer belongs to the program. For this reason, it's a good idea to set the pointer to `NULL` afterwards, so accidental later use is easier to spot.

```c
free(ptr);
ptr = NULL;   /* prevents accidental use of the invalid pointer */
```

## Keeping the Original Address

An allocated buffer can be used like an array. The following program allocates space for 20 integers, fills each element with a value and prints the values:

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *buffer;
    int x;

    buffer = malloc(sizeof(int) * 20);

    if (buffer == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }

    for (x = 0; x < 20; x++) {
        *(buffer + x) = x + 1;
        printf("%d ", *(buffer + x));
    }

    putchar('\n');

    free(buffer);

    return 0;
}
```

What matters here is how the program reaches each element. It doesn't change the pointer `buffer`. Instead, it calculates each element's address as `buffer + x` using **pointer arithmetic**.

The reason for doing it this way is that `free` needs **exactly the address that `malloc` returned**. If you moved the pointer itself forward, for example with `buffer++`, the original address would be lost. A later `free(buffer)` would then get the wrong address, which leads to **undefined behavior**: the program may crash, produce wrong results or seem to keep working correctly.

```c
/* WRONG: the pointer is moved and the original address is lost */
for (x = 0; x < 20; x++) {
    *buffer = x + 1;
    buffer++;
}

free(buffer);   /* wrong address: undefined behavior */
```

## Allocating Zeroed Memory: calloc

The **`calloc`** function (short for *contiguous allocation*) also allocates memory on the heap, but it differs from `malloc` in two ways. First, it takes two arguments: the **number of elements** and the **size of a single element**. Second, it sets every allocated byte to **zero**, so the memory contains no random leftover values. Like `malloc`, `calloc` returns `NULL` if it fails.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *ptr = calloc(5, sizeof(int));
    int i;

    if (ptr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    for (i = 0; i < 5; i++) {
        printf("%d ", ptr[i]);   /* output: 0 0 0 0 0 */
    }

    putchar('\n');

    free(ptr);

    ptr = NULL;

    return 0;
}
```

## Changing the Size: realloc

The **`realloc`** function (short for *reallocation*) changes the size of a memory block that has already been allocated. You can use it to make the block larger or smaller. The existing contents are kept, as far as they fit into the new block. Sometimes `realloc` has to move the block to a different place in memory, so it returns a new address.

There is an important trap here. If `realloc` fails, it returns `NULL`, **but the original memory block stays allocated and unchanged**. If you write the result straight back into the original pointer, as in `ptr = realloc(ptr, ...)`, a failure overwrites the only known address of the old block with `NULL`. That memory can then never be released. This is why you use a **temporary pointer** and only take over its value once the reallocation has succeeded:

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *ptr;
    int *temp;
    int i;

    ptr = malloc(5 * sizeof(int));

    if (ptr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    for (i = 0; i < 5; i++) {
        *(ptr + 1) = i + 1;
    }

    /* grow the block to 10 elements */
    temp = realloc(ptr, 10 * sizeof(int));

    if (temp == NULL) {
        printf("Memory reallocation failed\n");
        free(ptr);   /* the old block is still valid and is released */
        return 1;
    }

    ptr = temp;

    for (i = 5; i < 10; i++) {
        *(ptr + 1) = i + 1;
    }

    for (i = 0; i < 10; i++) {
        printf("%d ", *(ptr + 1));   /* output: 1 2 3 4 5 6 7 8 9 10 */
    }

    putchar('\n');

    free(ptr);

    return 0;
}
```

With `realloc`, you can build **dynamically growing arrays** that adjust to the number of elements they hold. The next section includes an example.

## When Do You Actually Need Memory Allocation?

Most of the time, you don't. If you know the size of the data when you write the code, the data is small and you only need it inside one function, an ordinary local variable is the better choice. Dynamic memory management is mainly worth it in five common situations.

### Situation 1: The Size Is Only Known at Runtime

A user says how many values they want to enter, or the program loads a file of unknown size. With `malloc`, you allocate exactly as much memory as you really need:

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int count;
    int *values;
    int i;

    if (scanf("%d", &count) != 1 || count <= 0) {
        return 1;
    }

    values = malloc(count * sizeof *values);   /* exactly as many as needed */

    if (values == NULL) {
        return 1;
    }

    for (i = 0; i < count; i++) {
        scanf("%d", &values[i]);
    }

    free(values);

    return 0;
}
```

The expression `sizeof *values` gives the size of the element the pointer refers to. If you change the pointer's data type later, the calculation is still correct.

You could simply write `int values[count];` instead. Since the C99 standard, C has allowed these **variable-length arrays** (**VLAs**). However, Microsoft's widely used compiler **MSVC** doesn't support them, and since C11 the standard treats them as optional. They also live on the small stack, so a large value for `count` can crash the program (see Situation 4).

### Situation 2: The Data Must Outlive the Function

Local variables are destroyed when a function ends. If a function returns the address of a local variable, that address points to memory that no longer exists. A pointer like this is called a **dangling pointer**. Memory on the heap, on the other hand, stays allocated until it is explicitly released. A typical case is a function that builds a string and returns it:

```c
#include <stdio.h>
#include <stdlib.h>

/* WRONG: buf is destroyed when the function returns */
char *makeGreetingWrong(const char *name) {
    char buf[64];
    sprintf(buf, "Hello %s", name);
    return buf;   /* address of memory that no longer exists */
}

/* RIGHT: heap memory survives, and the caller releases it */
char *makeGreeting(const char *name) {
    char *buf = malloc(64);

    if (buf == NULL) {
        return NULL;
    }

    snprintf(buf, 64, "Hello %s", name);

    return buf;
}

int main(void) {
    char *g = makeGreeting("Bob");

    if (g != NULL) {
        printf("%s\n", g);
        free(g);   /* the caller's job */
    }

    return 0;
}
```

With this technique, it must be clear who releases the memory. In this example, it's the **caller**, the code that calls the function. The same idea applies when you pass data to a **thread**, a part of the program that runs in parallel and may keep working after the function that started it has returned.

### Situation 3: A Collection That Grows

Suppose a program has to record every message it receives from a **CAN bus**. The CAN bus is a communication system that the control units in a vehicle use to exchange data. How many messages will arrive is unknown in advance. The solution is a **dynamically growing array**: you start with a little space and enlarge the array with `realloc` whenever it fills up. Java's `ArrayList` and Python's `list` work the same way internally.

```c
#include <stdint.h>
#include <stdlib.h>

typedef struct {
    uint32_t id;
    uint8_t  data[8];
} CanFrame;

CanFrame *frames = NULL;
size_t count = 0;
size_t capacity = 0;

int addFrame(CanFrame f) {
    if (count == capacity) {
        size_t newCap = (capacity == 0) ? 16 : capacity * 2;

        CanFrame *tmp = realloc(frames, newCap * sizeof *tmp);

        if (tmp == NULL) {
            return 1;   /* the old data is still valid */
        }

        frames = tmp;
        capacity = newCap;
    }

    frames[count++] = f;
    return 0;
}

/* when done: free(frames); */
```

The **capacity**, meaning the amount of space allocated, doubles every time the array grows. As a result, `realloc` only needs to be called rarely, even when many elements are added. By the way, `realloc` also accepts `NULL` as its first argument and then behaves like `malloc`. That's why the very first call needs no special handling.

### Situation 4: Large Amounts of Data

Because the stack is small, a large local array causes a **stack overflow**, and the program crashes. Large buffers, such as those for image data, therefore belong on the heap:

```c
#include <stdint.h>
#include <stdlib.h>

void process(void) {
    /* WRONG: 10 MB on a stack of about 1 MB causes a crash */
    /* uint8_t image[10 * 1024 * 1024]; */

    /* RIGHT: the heap can hold this much data */
    uint8_t *image = malloc(10 * 1024 * 1024);

    if (image == NULL) {
        return;
    }

    /* ... process the image data ... */

    free(image);
}
```

### Situation 5: Linked Lists, Trees and Queues

Some data structures are made of separate **nodes** that you create one at a time, only when you need them. In a **linked list**, each node holds a value and a pointer to the next node. Each new node is created with `malloc`:

```c
#include <stdlib.h>

typedef struct Node {
    int value;
    struct Node *next;   /* pointer to the next node */
} Node;

Node *push(Node *head, int value) {
    Node *n = malloc(sizeof *n);

    if (n == NULL) {
        return head;
    }

    n->value = value;
    n->next  = head;

    return n;   /* new head of the list */
}

void freeList(Node *head) {
    while (head != NULL) {
        Node *next = head->next;
        free(head);
        head = next;
    }
}
```

The arrow operator `->` accesses a field of a structure through a pointer. When cleaning up, you have to release each node separately. You also have to save the address of the next node **before** releasing the current one.

## The Most Important Rules

If you use dynamic memory, stick to three basic rules:

1. **Check for `NULL` after every call to `malloc`, `calloc` or `realloc`.** Only use the memory after this check.
2. **Every allocation needs exactly one `free`.** Forgetting it causes a memory leak. Releasing the same memory twice can crash the program.
3. **Never use memory after it has been released.** Setting the pointer to `NULL` after `free` helps you catch these mistakes early.

## Common Mistakes

Dynamic memory management is flexible, but handling it incorrectly leads to errors that are often hard to find. A **memory leak** happens when a program never releases memory it has allocated. In short programs, this is barely noticeable. A program that runs for a long time, however, keeps using more and more memory until the system's resources run out.

A **dangling pointer** refers to memory that has already been released. If the program uses it anyway, the result is undefined behavior, anything from wrong values to a crash. These errors are especially tricky because the program sometimes seems to keep working correctly.

When a program allocates and releases memory very often, **fragmentation** can occur. The heap breaks up into many small free gaps between used blocks. In total, there may still be enough free memory, but no single contiguous block is large enough for a new request. Finally, if an **allocation failure** goes unhandled because the `NULL` check was forgotten, the program uses an invalid address and usually crashes.

## A Note on Embedded Systems

In **embedded systems**, such as the control units in a vehicle, dynamic memory management is usually **forbidden**. The coding standard **MISRA C:2012**, which is widely used in the automotive industry, bans `malloc` and its related functions in **Rule 21.3**. The reason is that heap allocation can fail or fragment memory at runtime, and this kind of unpredictable behavior is unacceptable in safety-critical systems. Instead, embedded code uses **fixed-size static buffers**, whose memory needs are known at compile time. For programs on ordinary desktop computers, such as a diagnostic tool running on Windows, `malloc` is perfectly fine.

## Conclusion

Dynamic memory management lets a C program request exactly as much memory as it needs while it runs. `malloc` allocates an uninitialized block, `calloc` allocates a zero-filled block, `realloc` changes the size of an existing block, and `free` releases memory. All four functions are declared in `stdlib.h` and work on the heap, which is much larger than the stack.

What matters most is using these functions carefully. Check every result for `NULL`, keep the original address for `free`, use a temporary pointer with `realloc` and release every allocated block exactly once. Dynamic memory is worth using when the size is only known at runtime, the data must outlive a function, a collection grows, large amounts of data are involved or structures like linked lists are built. In all other cases, an ordinary local variable is the simpler and safer choice.

---

*Sources:*

- *LinkedIn Learning course "Complete Guide to C Programming Foundations" by Dan Gookin*
- *[Dynamic Memory Allocation in C](https://www.geeksforgeeks.org/c/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/)*
