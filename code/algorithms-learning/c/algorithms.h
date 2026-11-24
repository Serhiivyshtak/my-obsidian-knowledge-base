#ifndef ALGORITHMS_H
    #define ALGORITHMS_H

    typedef struct {
        int* items;
        int capacity;
        int front;
        int size;
    } CircularQueue;

    int initializeQueue(CircularQueue* queue, int queueCapacity);
    void destroyQueue(CircularQueue* queue);
    int enqueue(CircularQueue* queue, int newItem);
    int dequeue(CircularQueue* queue, int* removedItem);
    void printQueue(CircularQueue* queue);


    int linearSearch(int array[], int arrayLength, int searchedItem);
    int binarySearch(int array[], int arrayLength, int searchedItem);
#endif