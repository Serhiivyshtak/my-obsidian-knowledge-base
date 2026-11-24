#include "algorithms.h"
#include <stdio.h>
#include <stdlib.h>


// -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
int initializeQueue(CircularQueue* queue, int queueCapacity) {
    queue->items = NULL;
    queue->capacity = queue->front = queue->size = 0;

    if (queueCapacity <= 0) {
        printf("ERROR: Couldn't initialize a queue due to invalid queue capacity (%d)\n", queueCapacity);
        return 1;
    }

    queue->items = malloc(queueCapacity * sizeof(int));

    if (queue->items == NULL) {
        printf("ERROR: Couldn't initialize a queue due to memory allocation error\n");
        return 1;
    }

    queue->capacity = queueCapacity;
    queue->front = 0;
    queue->size = 0;

    return 0;
}


// -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
void destroyQueue(CircularQueue* queue) {
    free(queue->items);
    queue->items = NULL;
    queue->capacity = queue->front = queue->size = 0;
}


// -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
const int isQueueEmpty(CircularQueue* queue) {
    return queue->size == 0;
}

// -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
const int isQueueFull(CircularQueue* queue) {
    return queue->size == queue->capacity;
}


// -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
int enqueue(CircularQueue* queue, int newItem) {
    if (isQueueFull(queue)) {
        printf("ERROR: Couldn't enqueue item %d because the queue is full\n", newItem);
        return 1;
    }

    int newItemIndex;

    if ((queue->front + queue->size) < queue->capacity) {
        newItemIndex = queue->front + queue->size;
    } else {
        newItemIndex = queue->front + queue->size - queue->capacity;
    }

    queue->items[newItemIndex] = newItem;
    queue->size++;
    return 0;
}


// -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
int dequeue(CircularQueue* queue, int* removedItem) {
    if (isQueueEmpty(queue)) {
        printf("ERROR: Couldn't dequeue because the queue is empty\n");
        return 1;
    }

    int newFront;

    if (queue->front + 1 == queue->capacity) {
        newFront = 0;
    } else {
        newFront = queue->front + 1;
    }

    if (removedItem != NULL) {
        *removedItem = queue->items[queue->front];
    }

    queue->front = newFront;
    queue->size--;
    return 0;
}


// -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
void printQueue(CircularQueue* queue) {
    if (isQueueEmpty(queue)) {
        printf("The queue is empty\n");
        return;
    }

    printf("CircularQueue contents:\n");

    for (int i = 0; i < queue->size; i++) {
        int index = (queue->front + i) % queue->capacity;
        printf("%d: %d\n", index, queue->items[index]);
    }
}


// -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
int linearSearch(int array[], int arrayLength, int searchedItem) {
    for (int i = 0; i < arrayLength; i++) {
        if (array[i] == searchedItem) {
            return i;
        }
    }

    return -1;
}


// -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
int binarySearch(int array[], int arrayLength, int searchedItem) {
    int lowBoundary = 0;
    int highBoundary = arrayLength - 1;
    int middle;

    while (lowBoundary <= highBoundary) {
        middle = lowBoundary + (highBoundary - lowBoundary) / 2;

        if (array[middle] == searchedItem) {
            return middle;
        } else if (array[middle] < searchedItem) {
            lowBoundary = middle + 1;
        } else {
            highBoundary = middle - 1;
        }
    }

    return -1;
}