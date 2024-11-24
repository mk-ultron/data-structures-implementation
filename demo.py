from linked_lists import Stack, Queue, test_performance

def demonstrate_stack():
    """
    Demonstrates basic Stack operations (LIFO behavior).
    Shows insertion and removal of elements with current state after each operation.
    """
    print("\n=== Stack Demonstration (LIFO) ===")
    stack = Stack()
    
    print("Adding numbers 1, 2, 3 to stack...")
    for i in range(1, 4):
        stack.insert(i)
        print(f"After inserting {i}:")
        stack.print()
    
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
    
    print("Adding numbers 1, 2, 3 to queue...")
    for i in range(1, 4):
        queue.insert(i)
        print(f"After inserting {i}:")
        queue.print()
    
    print("\nRemoving elements from queue:")
    for _ in range(3):
        removed = queue.remove()
        print(f"Removed: {removed}")
        print("Current queue:")
        queue.print()

def manual_verification_test():
    """
    Quick test to manually verify stack and queue operations
    """
    print("\nManual Verification Test")
    print("========================")
    
    # Test Stack
    print("\nTesting Stack:")
    stack = Stack()
    
    # Add 5 elements and verify
    print("Adding elements 1-5...")
    for i in range(1, 6):
        stack.insert(i)
    print("Stack contents:")
    stack.print()
    
    # Remove and verify
    print("\nRemoving elements (should be in reverse order):")
    while True:
        value = stack.remove()
        if value is None:
            break
        print(f"Removed: {value}")
    
    # Test Queue
    print("\nTesting Queue:")
    queue = Queue()
    
    # Add 5 elements and verify
    print("Adding elements 1-5...")
    for i in range(1, 6):
        queue.insert(i)
    print("Queue contents:")
    queue.print()
    
    # Remove and verify
    print("\nRemoving elements (should be in order):")
    while True:
        value = queue.remove()
        if value is None:
            break
        print(f"Removed: {value}")

if __name__ == "__main__":
    print("Starting Data Structure Demonstrations")
    
    # Run original demonstrations
    demonstrate_stack()
    demonstrate_queue()
    
    # Run manual verification test
    manual_verification_test()
    
    # Run performance tests
    print("\n=== Performance Testing ===")
    print("Testing insertion and deletion of 100, 1000, and 10000 elements...")
    test_performance()