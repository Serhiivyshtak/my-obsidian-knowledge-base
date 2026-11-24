#include <stdio.h>
#include "algorithms.h"


int main() {
    // int array[] = {12, 3, 43, 234, 5, 43, 1, 343, 14, 767, 34, 45};
    // int arrayLength = sizeof(array) / sizeof(int);

    // printf("%d", linearSearch(array, arrayLength, 1));

    // -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    CircularQueue queue;

    int queueInitializationStatus = initializeQueue(&queue, 5);

    if (queueInitializationStatus) {
        return 1;
    }

    enqueue(&queue, 5);
    enqueue(&queue, 10);
    enqueue(&queue, 15);
    enqueue(&queue, 20);
    enqueue(&queue, 25);
    
    printQueue(&queue);

    dequeue(&queue, NULL);
    dequeue(&queue, NULL);
    
    printQueue(&queue);

    enqueue(&queue, 30);
    enqueue(&queue, 35);

    printQueue(&queue);

    destroyQueue(&queue);

    return 0;
}