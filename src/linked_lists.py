import time
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def remove(self):
        if not self.tail:
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data
    
    def print(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def remove(self):
        if not self.head:
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data
    
    def print(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def test_performance():
    sizes = [100, 1000, 10000]
    structures = {
        'Stack': Stack(),
        'Queue': Queue()
    }
    
    results = {
        'Insert': {size: {} for size in sizes},
        'Delete': {size: {} for size in sizes}
    }
    
    for name, structure in structures.items():
        for size in sizes:
            # Test insertion
            numbers = [random.randint(1, 10000) for _ in range(size)]
            
            start_time = time.time()
            for num in numbers:
                structure.insert(num)
            end_time = time.time()
            results['Insert'][size][name] = round((end_time - start_time) * 1000, 2)
            
            # Test deletion
            start_time = time.time()
            for _ in range(size):
                structure.remove()
            end_time = time.time()
            results['Delete'][size][name] = round((end_time - start_time) * 1000, 2)
    
    # Print results in table format
    print("\nPerformance Results (time in milliseconds):")
    print("=" * 70)
    print(f"{'Object / Code':<15} | {'Insert':->20} | {'Delete':->20}")
    print(f"{'':<15} | {'100':>6} {'1000':>6} {'10000':>6} | {'100':>6} {'1000':>6} {'10000':>6}")
    print("-" * 70)
    
    for struct_name in structures.keys():
        row = f"{struct_name:<15} |"
        for size in sizes:
            row += f" {results['Insert'][size][struct_name]:>5.1f}"
        row += " |"
        for size in sizes:
            row += f" {results['Delete'][size][struct_name]:>5.1f}"
        print(row)

if __name__ == "__main__":
    test_performance()