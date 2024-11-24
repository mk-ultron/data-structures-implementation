# Data Structures Implementation: Stack and Queue

This project implements Stack and Queue data structures using doubly-linked lists in Python. It includes comprehensive testing and performance analysis for both data structures.

## Overview

Both Stack and Queue are implemented using a doubly-linked list structure, with each implementation containing three main operations:
- Insert: Adds elements to the data structure
- Remove: Removes elements from the data structure
- Print: Displays the current contents

### Stack (LIFO - Last In, First Out)
- Insert: Adds elements to the end of the stack (O(1))
- Remove: Removes elements from the end of the stack (O(1))
- Elements are removed in reverse order of insertion

### Queue (FIFO - First In, First Out)
- Insert: Adds elements to the end of the queue (O(1))
- Remove: Removes elements from the front of the queue (O(1))
- Elements are removed in the same order they were inserted

## Implementation Details

### Node Class
```python
class Node:
    def __init__(self, data):
        self.data = data      # The actual value stored in the node
        self.next = None      # Reference to the next node
        self.prev = None      # Reference to the previous node
```

### Key Operations
Both Stack and Queue implementations include:
- `insert(data)`: Creates and adds a new node with the given data
- `remove()`: Removes and returns data from the appropriate end based on the data structure
- `print()`: Displays the contents in a readable format

## Performance Analysis

Performance testing was conducted on both data structures with different sizes (100, 1,000, and 10,000 elements). Key findings:

1. Insert vs Delete Operations:
   - Insertion operations are consistently slower than deletion operations
   - This is likely due to memory allocation and node creation overhead during insertion
   - Deletion primarily involves pointer manipulation and is generally more efficient

2. Queue vs Stack Comparison:
   - In my testing queue operations consistently performed faster than stack operations
   - Queue's combination of tail insertion and head removal appears to be more efficient
   - Memory locality may be better optimized in queue operations

3. Scaling Characteristics:
   - Both structures show linear time complexity O(1) for their operations
   - Performance scales pretty predictably with input size
   - Memory management and system overhead become more noticeable at larger sizes

### Sample Performance Results
```
Performance Results (time in milliseconds):
Object / Code    | ----------Insert---------- | ----------Delete----------
                |   100   1000  10000 |   100   1000  10000
----------------------------------------------------------
Stack           |   0.0    1.0    2.1 |   0.0    0.0    1.0
Queue           |   0.0    0.0    2.0 |   0.0    0.0    0.0
```

## Usage

```python
# Stack Example
stack = Stack()
stack.insert(1)
stack.insert(2)
stack.print()  # Output: 1 -> 2 -> None
stack.remove() # Returns 2 (LIFO)

# Queue Example
queue = Queue()
queue.insert(1)
queue.insert(2)
queue.print()  # Output: 1 -> 2 -> None
queue.remove() # Returns 1 (FIFO)
```

## Testing
The project includes:
- Basic operation demonstrations
- Manual verification tests
- Performance testing with different data sizes
- Validation of insert and remove operations

To run all tests:
```python
python demo.py
```

## Future Improvements
Potential enhancements could include:
- Implementation of object pools for better memory management
- Additional operations (peek, size, isEmpty)
- Thread-safe implementations
- Memory usage optimization
- Extended performance testing with larger datasets