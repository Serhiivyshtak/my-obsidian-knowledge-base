#include <stdio.h>
#include "algorithms.h"


int main() {
    int array[] = {12, 3, 43, 234, 5, 43, 1, 343, 14, 767, 34, 45};
    int arrayLength = sizeof(array) / sizeof(int);

    printf("%d", linearSearch(array, arrayLength, 1));

    return 0;
}