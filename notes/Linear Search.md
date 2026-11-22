# Linear Search

**Linear Search** is a sequential searching [[Data Structures & Algorithms|algorithm]] used in computer science to locate a target value within an **array** (a contiguous collection of elements indexed by position) and return its corresponding index. Unlike sorting algorithms, which alter the arrangement of elements within a data structure, searching algorithms such as Linear Search inspect elements without modifying the underlying array.

## Operational Mechanism

The algorithm executes sequentially from the beginning of the array to the end using the following procedure:

1. Start at the initial element (index `0`) and iterate sequentially through each subsequent position in the array.
2. Compare the element at the current index against the target value.
3. Terminate the search immediately and return the current index if the element matches the target value.
4. Return `-1` as a sentinel value indicating failure if the algorithm reaches the end of the array without encountering a match.

## Execution Walkthrough

Consider searching for the target value `11` within the zero-indexed array `[12, 8, 9, 11, 5, 11]`. At index `0`, the algorithm evaluates `12 == 11`, which is false. It advances to index `1` (`8 == 11`, false) and subsequently to index `2` (`9 == 11`, false). Upon reaching index `3`, the algorithm evaluates `11 == 11`, which is true. Execution halts immediately and returns index `3`, leaving the duplicate value `11` at index `5` uninspected.

## Time Complexity Analysis

The computational efficiency of Linear Search scales linearly with the number of elements $n$ in the array. In the **best-case scenario**, where the target value resides at index `0`, the algorithm terminates after a single comparison. In the **worst-case scenario**—occurring when the target value is located at the final index ($n - 1$) or is absent from the array entirely—the algorithm must perform $n$ comparisons. Consequently, the worst-case time complexity of Linear Search is expressed in Big O notation as $O(n)$.

## Advantages, Disadvantages, and Algorithmic Comparisons

Linear Search offers distinct operational trade-offs compared to other searching mechanisms. The primary advantage of Linear Search is its inherent simplicity, making it straightforward to implement and debug. Furthermore, it operates independently of the data's initial state, meaning it requires no preprocessing, sorting, or structural ordering of the collection before execution. It can be applied universally to both arrays and linked lists, and it leaves the underlying data structure completely unmodified.

The primary disadvantage of Linear Search is its poor scalability on large datasets. Because its time complexity is $O(n)$, execution time scales directly with the number of elements, resulting in substantial performance degradation for massive collections.

When compared to **Binary Search**, Linear Search is generally less efficient for large datasets because Binary Search achieves a logarithmic time complexity of $O(\log n)$. However, Binary Search has a strict prerequisite: the underlying array must be sorted prior to execution, and it requires efficient random access, rendering it suboptimal for data structures like linked lists. Conversely, if a dataset is small, unsorted, or frequently modified with insertions and deletions, the computational overhead required to sort the data for Binary Search often outweighs the search efficiency gained, making Linear Search the more practical choice under those specific conditions.

*Based on the W3Schools article [DSA Linear Search](https://www.w3schools.com/dsa/dsa_algo_linearsearch.php)*