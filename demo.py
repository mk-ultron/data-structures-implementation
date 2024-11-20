# demo.py
from linked_lists import Stack, Queue, test_performance

def demonstrate_stack():
    """
    Demonstrates basic Stack operations (LIFO behavior).
    Shows insertion and removal of elements with current state after each operation.
    """
    print("\n=== Stack Demonstration (LIFO) ===")
    stack = Stack()
    
    # Demonstrate insertion
    print("Adding numbers 1, 2, 3 to stack...")
    for i in range(1, 4):
        stack.insert(i)
        print(f"After inserting {i}:")
        stack.print()
    
    # Demonstrate removal
    print("\nRemoving elements from stack:")
    for _ in range(3):
        removed = stack.remove()
        print(f"Removed: {removed}")
        print("Current stack:")
        stack.print()

def demonstrate_queue():
    """
    Demonstrates basic Queue operations (FIFO behavior).
    Shows insertion and removal of elements with current state after each operation.
    """
    print("\n=== Queue Demonstration (FIFO) ===")
    queue = Queue()
    
    # Demonstrate insertion
    print("Adding numbers 1, 2, 3 to queue...")
    for i in range(1, 4):
        queue.insert(i)
        print(f"After inserting {i}:")
        queue.print()
    
    # Demonstrate removal
    print("\nRemoving elements from queue:")
    for _ in range(3):
        removed = queue.remove()
        print(f"Removed: {removed}")
        print("Current queue:")
        queue.print()

if __name__ == "__main__":
    # Main demonstration sequence
    print("Starting Data Structure Demonstrations")
    
    # Run stack demonstration
    demonstrate_stack()
    
    # Run queue demonstration
    demonstrate_queue()
    
    # Run performance tests
    print("\n=== Performance Testing ===")
    print("Testing insertion and deletion of 100, 1000, and 10000 elements...")
    test_performance()