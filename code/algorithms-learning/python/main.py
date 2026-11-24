from algorithms import linear_search, binary_search, CircularQueue


# array = [12, 3, 43, 234, 5, 43, 1, 343, 14, 767, 34, 45]

# print(linear_search(array, 1))

# array.sort()

# print(binary_search(array, 1))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

queue = CircularQueue(5)

queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
queue.enqueue(20)
queue.enqueue(25)

queue.printQueue()

queue.dequeue()
queue.dequeue()

queue.printQueue()

queue.enqueue( 30)
queue.enqueue( 35)

queue.printQueue()