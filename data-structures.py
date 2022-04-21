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


# Stack - Simply create list
stack = []
## Push - append(), O(1)
stack.append(1)

## Pop - pop(), O(1)
stack.pop()

## Size - len(), O(1)
len(stack)

## Top
### Depending which side is considered the front
stack[0]
stack[-1]

# Queue

# Hash Table

# Hash Set

# Tree

# Priority Queue and Graph
