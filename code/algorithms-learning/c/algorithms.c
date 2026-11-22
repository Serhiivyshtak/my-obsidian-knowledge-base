#include "algorithms.h"


// --------------------------------------------------------------------------------------------------------------------------------------------------------------------
int linearSearch(int array[], int arrayLength, int searchedItem) {
    for (int i = 0; i < arrayLength; i++) {
        if (array[i] == searchedItem) {
            return i;
        }
    }

    return -1;
}


// --------------------------------------------------------------------------------------------------------------------------------------------------------------------
int binarySearch(int array[], int arrayLength, int searchedItem) {
    int lowBoundary = 0;
    int hightBoundary = arrayLength - 1;
    int middle;

    while (lowBoundary <= hightBoundary) {
        middle = lowBoundary + (hightBoundary - lowBoundary) / 2;

        if (array[middle] == searchedItem) {
            return middle;
        } else if (array[middle] < searchedItem) {
            lowBoundary = middle + 1;
        } else {
            hightBoundary = middle - 1;
        }
    }

    return -1;
}