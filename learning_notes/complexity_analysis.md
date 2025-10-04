# Big O Notation: Time and Space Complexity

## Simplified concepts

- How fast it runs? *Time Complexity*
- How much space does it consume? *Space Complexity*

## Big O Notation

Big O Notation is a way of describing the efficiency of a piece of code (usually a function)

The “O” in Big O stands for “order of” and the “f(n)” represents the function that defines the growth rate of the algorithm as a function of the input size. The function f(n) can be any mathematical expression or formula that represents the number of operations performed or the amount of memory used by the algorithm.

### Time Complexity
Time complexity in Big O notation is a measure of how an algorithm’s running time increases with the size of its input. It provides an estimate of the worst-case time required to execute an algorithm as a function of the input size. In other words, it gives us an upper bound on the time taken by the algorithm to complete its task.

There are several common time complexities expressed using Big O notation:

- O(1) — Constant Time: The algorithm’s running time does not depend on the size of the input; it performs a fixed number of operations.
- O(log n) — Logarithmic Time: The algorithm’s running time grows logarithmically with the size of the input.
- O(n) — Linear Time: The algorithm’s running time scales linearly with the size of the input.
- O(n log n) — Linearithmic Time: The algorithm’s running time grows in proportion to n times the logarithm of n.
- O(n²) — Quadratic Time: The algorithm’s running time is directly proportional to the square of the input size.
- O(2^n) — Exponential Time: The algorithm’s running time doubles with each increase in the input size.


### Space Complexity
Space complexity in Big O notation measures the amount of memory used by an algorithm with respect to the size of its input. It represents the worst-case memory consumption as the input size increases.

Similar to time complexity, space complexity also has different notations:

- O(1) — Constant Space: The algorithm uses a fixed amount of memory that does not depend on the input size.
- O(n) — Linear Space: The algorithm’s memory usage grows linearly with the input size.
- O(n²) — Quadratic Space: The algorithm’s memory usage increases proportionally to the square of the input size.

Extracted from: https://medium.com/@DevChy/introduction-to-big-o-notation-time-and-space-complexity-f747ea5bca58