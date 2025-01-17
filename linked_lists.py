# linked_lists.py
import time
import random

class Node:
    """
    Node class for doubly-linked list implementation.
    Each node contains data and references to the next and previous nodes.
    """
    def __init__(self, data):
        self.data = data      # The actual value stored in the node
        self.next = None      # Reference to the next node
        self.prev = None      # Reference to the previous node

class Stack:
    """
    Stack implementation using a doubly-linked list.
    Follows LIFO (Last In, First Out)
    """
    def __init__(self):
        self.head = None      # First node in the stack
        self.tail = None      # Last node in the stack (where we add/remove elements)
        
    def insert(self, data):
        """
        Inserts a new element at the end of the stack (top).
        Time complexity: O(1)
        """
        new_node = Node(data)
        if not self.head:  # If stack is empty
            self.head = new_node
            self.tail = new_node
        else:  # Add to the end (top) of stack
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def remove(self):
        """
        Removes and returns the last element added (top of stack).
        Time complexity: O(1)
        Returns: None if stack is empty, otherwise the data from the removed node
        """
        if not self.tail:  # If stack is empty
            return None
        data = self.tail.data
        if self.head == self.tail:  # If only one node
            self.head = None
            self.tail = None
        else:  # Remove from end (top) of stack
            self.tail = self.tail.prev
            self.tail.next = None
        return data
    
    def print(self):
        """
        Prints the stack contents from bottom to top.
        Format: item1 -> item2 -> ... -> itemN -> None
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

class Queue:
    """
    Queue implementation using a doubly-linked list.
    Follows FIFO (First In, First Out)
    """
    def __init__(self):
        self.head = None      # Front of queue (where we remove elements)
        self.tail = None      # Back of queue (where we add elements)
        
    def insert(self, data):
        """
        Inserts a new element at the end of the queue.
        Time complexity: O(1)
        """
        new_node = Node(data)
        if not self.head:  # If queue is empty
            self.head = new_node
            self.tail = new_node
        else:  # Add to end of queue
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def remove(self):
        """
        Removes and returns the first element in the queue.
        Time complexity: O(1)
        Returns: None if queue is empty, otherwise the data from the removed node
        """
        if not self.head:  # If queue is empty
            return None
        data = self.head.data
        if self.head == self.tail:  # If only one node
            self.head = None
            self.tail = None
        else:  # Remove from front of queue
            self.head = self.head.next
            self.head.prev = None
        return data
    
    def print(self):
        """
        Prints the queue contents from front to back.
        Format: item1 -> item2 -> ... -> itemN -> None
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def test_performance():
    """
    Tests the performance of Stack and Queue operations with different sizes.
    Includes validation and more detailed output.
    """
    sizes = [100, 1000, 10000]
    
    # Dictionary to store results
    results = {
        'Insert': {size: {} for size in sizes},
        'Delete': {size: {} for size in sizes}
    }
    
    for name in ['Stack', 'Queue']:
        print(f"\nTesting {name}:")
        for size in sizes:
            print(f"\nSize: {size} elements")
            
            # Create fresh instance
            structure = Stack() if name == 'Stack' else Queue()
            
            # Generate random numbers
            numbers = [random.randint(1, 10000) for _ in range(size)]
            
            # Test insertion
            start_time = time.time()
            
            # Insert elements and validate count
            count = 0
            for num in numbers:
                structure.insert(num)
                count += 1
            
            end_time = time.time()
            insert_time = round((end_time - start_time) * 1000, 2)
            results['Insert'][size][name] = insert_time
            
            # Validate insertion
            print(f"Inserted {count} elements in {insert_time}ms")
            
            # Test deletion
            start_time = time.time()
            
            # Delete elements and validate count
            removed_count = 0
            while structure.remove() is not None:
                removed_count += 1
            
            end_time = time.time()
            delete_time = round((end_time - start_time) * 1000, 2)
            results['Delete'][size][name] = delete_time
            
            # Validate deletion
            print(f"Removed {removed_count} elements in {delete_time}ms")
            
            # Verify counts match
            if count != size or removed_count != size:
                print(f"WARNING: Count mismatch! Expected {size}, "
                      f"Inserted {count}, Removed {removed_count}")
    
    # Print final results table
    print("\nPerformance Results (time in milliseconds):")
    print("=" * 70)
    print(f"{'Object / Code':<15} | {'Insert':->20} | {'Delete':->20}")
    print(f"{'':<15} | {'100':>6} {'1000':>6} {'10000':>6} | {'100':>6} {'1000':>6} {'10000':>6}")
    print("-" * 70)
    
    for struct_name in ['Stack', 'Queue']:
        row = f"{struct_name:<15} |"
        for size in sizes:
            row += f" {results['Insert'][size][struct_name]:>5.1f}"
        row += " |"
        for size in sizes:
            row += f" {results['Delete'][size][struct_name]:>5.1f}"
        print(row)