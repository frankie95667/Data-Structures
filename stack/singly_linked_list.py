class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            new_node.set_next(None)
        else:
            self.tail.set_next(new_node)
            new_node.set_next(None)
            self.tail = new_node

    def remove_head(self):
        if self.head is None:
            return None
        data = self.head.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
        return data
    
    def contains(self, value):
        current = self.head
        if current is None:
            return None
        while current != None:
            if current.value == value:
                return True
            current = current.get_next()
        return False
    
    def get_max(self):
        current = self.head
        if current is None:
            return None
        max = current.value
        while current.get_next() != None:
            if max < current.get_next().value:
                current = current.get_next()
                max = current.value
            else:
                current = current.get_next()
        return max