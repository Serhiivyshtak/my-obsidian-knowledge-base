# Binary Search Algorithm

**Binary Search** is an efficient searching [[Data Structures & Algorithms|algorithm]] designed to locate a target value within a sorted array by repeatedly dividing the search interval in half. If the target value is lower than the center element of the current search area, the algorithm restricts its subsequent search to the left half; if the target value is higher, it restricts to the right half. This exponential reduction of the search space ensures that Binary Search executes significantly faster than sequential search methods.

## Operational Mechanism

The algorithm executes through a repetitive subdivision process until the target value is located or the search area is exhausted. The step-by-step procedure is defined as follows:  

1. Check the value located in the exact center of the current array search area.
2. Compare the target value against the center value: if the target is lower, target the left sub-array; if the target is higher, target the right sub-array.
3. Repeat the center-checking and sub-array selection process on the newly reduced segment until the target value is found or the search area becomes empty.
4. Return the integer index of the target value if found, or return `-1` if the target value is absent from the array.

## Execution Walkthrough

Consider searching for the target value `11` within the sorted array `[2, 3, 7, 7, 11, 15, 25]`.  

1. The algorithm evaluates the middle element of the array at index `3`, which holds the value `7`.
2. Because `7` is less than `11`, the search is restricted to the right half of the array containing the elements `[11, 15, 25]`.
3. The next center element evaluated is `15` at index `5`.
4. Because `15` is greater than `11`, the search is restricted to the left of index `5`, leaving index `4` as the final remaining element to evaluate.
5. Index `4` contains the target value `11`, and the algorithm successfully terminates, returning index position `4`.

## Time Complexity Analysis

Because the search area is halved with every single comparison, Binary Search scales logarithmically with respect to the number of elements $n$ in the sorted array. In the worst-case scenario—where the target value is completely absent or located at the final remaining split—the algorithm requires at most $\log_2 n$ comparisons. While Big O notation often simplifies this to $O(\log n)$, retaining the base-2 notation $O(\log_2 n)$ explicitly emphasizes the fundamental concept that the search space is divided by two during each iterative comparison.  

## Advantages and Disadvantages

Binary Search provides exceptional search efficiency for static, ordered datasets, though its strict operational prerequisites introduce specific constraints compared to sequential search methods.

### Advantages

- **Logarithmic Time Complexity:** By eliminating half of the remaining elements during every iteration, Binary Search achieves a worst-case time complexity of $O(\log_2 n)$, allowing it to locate elements in massive datasets with minimal comparisons.
- **Minimal Space Complexity:** Iterative implementations of Binary Search operate in-place using only a few pointer variables (`low`, `high`, and `mid`), resulting in an $O(1)$ auxiliary space complexity.
- **Predictable Worst-Case Performance:** Unlike data structures that can degrade under specific input patterns, Binary Search guarantees a strictly bounded maximum number of steps ($\lfloor \log_2 n \rfloor + 1$) regardless of where the target value sits in the array.

### Disadvantages

- **Strict Sorting Prerequisite:** The input collection must be completely sorted prior to execution. If the data is unsorted, sorting it first typically incurs an $O(n \log n)$ computational overhead, which outweighs the search efficiency gained for single-lookup operations.
- **Requirement for Direct Random Access:** Binary Search relies on $O(1)$ constant-time indexing to jump directly to the midpoint of a search interval. Consequently, it is inefficient on data structures that lack random access, such as standard singly or doubly linked lists, where traversing to the middle node degrades performance to $O(n)$.
- **Overhead on Dynamic Datasets:** Maintaining sorted order in an array requires shifting elements during insertions and deletions ($O(n)$ time), making Binary Search suboptimal for datasets that undergo frequent structural modifications.

---

*Based on the W3Schools article [DSA Binary Search](https://www.w3schools.com/dsa/dsa_algo_binarysearch.php)*