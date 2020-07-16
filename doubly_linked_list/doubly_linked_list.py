"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1

        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        # self.length -= 1
        
        # if self.head.next is not None:
        #     self.head.next.prev = self.head.prev
        #     self.head = self.head.next

        # else:
        #     self.head = None
        #     self.tail = None
        self.delete(self.head)
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        # self.length -= 1
        
        # if self.tail.prev is not None:
        #     self.tail.prev.next = self.tail.next
        #     self.tail = self.tail.prev

        # else:
        #     self.head = None
        #     self.tail = None
        self.delete(self.tail)
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is None or self.head is None or self.head is node:
            return

        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is not None:
            node.prev.next = node.next

        node.next = self.head
        node.next.prev = node
        self.head = node
        self.head.prev = None
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is None or self.head is None:
            return

        if self.head is node:
            self.head = node.next
            self.head.prev = None

        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is not None:
            node.prev.next = node.next

        node.prev = self.tail
        node.prev.next = node
        self.tail = node 
        self.tail.next = None

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None or node is None:
            return

        self.length -= 1

        if self.head is node:
            self.head = node.next

        if self.head is None:
            self.tail = None

        if node.next is not None:
            node.next.prev = node.prev
        
        if node.prev is not None:
            node.prev.next = node.next
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):

        if self.head is None:
            return

        current = self.head
        max = 0
        while current != None:
            if max < current.value:
                max = current.value
            current = current.next
        return max