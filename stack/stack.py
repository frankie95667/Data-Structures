"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if not self.size:
            return None
        ele = self.storage.tail.value
        current = self.storage.head
        
        while current != None:
            if current.get_next() == self.storage.tail:
                self.storage.tail = current
                self.storage.tail.next = None
            current = current.get_next()
        self.size -= 1
        return ele
