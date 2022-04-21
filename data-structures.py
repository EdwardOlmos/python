"""Arrays - AKA 'Lists'
Time Complexity with index O(1)
Space Complexity O(n)
"""
array_a = [1, 2, 3]
print(array_a[-1])

# slicing - left INCLUSIVE, right EXCLUSIVE
array_a = [0, 10, 20, 30, 40, 50]
print(array_a[2:5])
print(array_a[1:])
print(array_a[:3])

for i, num in enumerate(array_a):
    print(i, num)

# Linked List
class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# Stack

# Queue

# Hash Table

# Hash Set

# Tree

# Priority Queue and Graph
