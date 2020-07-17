"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        if self.node is None:
            return

        if self.node.left is not None:
            self.node.left.update_height()

        if self.node.right is not None:
            self.node.right.update_height()

        if self.node.left:
            left_height = self.node.left.height
        else:
            left_height = -1

        if self.node.right:
            right_height = self.node.right.height
        else:
            right_height = -1
        
        self.height = max(left_height, right_height) + 1

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        if self.node is None:
            return

        if self.node.left is not None:
            self.node.left.update_balance()

        if self.node.right is not None:
            self.node.right.update_balance()

        if self.node.left:
            left_height = self.node.left.height
        else:
            left_height = -1

        if self.node.right:
            right_height = self.node.right.height
        else:
            right_height = -1
        
        self.balance = left_height - right_height

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        if self.node is None:
            return

        temp = self.node.left
        self.node.left = AVLTree(Node(self.node.key))
        self.node.left.node.left = temp
        
        if self.node.right.node.left is not None:
            self.node.left.node.right = self.node.right.node.left
        
        self.node.key = self.node.right.node.key
        self.node.right = self.node.right.node.right


    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        if self.node is None:
            return

        temp = self.node.right
        self.node.right = AVLTree(Node(self.node.key))
        self.node.right.node.right = temp
        
        if self.node.left.node.right is not None:
            self.node.right.node.left = self.node.left.node.right
        
        self.node.key = self.node.left.node.key
        self.node.left = self.node.left.node.left


    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        if self.node.left is not None:
            self.node.left.rebalance()
                
        if self.node.right is not None:
            self.node.right.rebalance()
        
        self.update_height()
        self.update_balance()

        if abs(self.balance) >= 2:
            if self.balance > 0:
                if self.node.left.balance >= 0:
                    self.right_rotate()
                else:
                    self.node.left.left_rotate()
                    self.right_rotate()
            else:
                if self.node.right.balance <= 0:
                    self.left_rotate()
                else:
                    self.node.right.right_rotate()
                    self.left_rotate()
                
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):

        queue = []
        queue.append(self)

        if self.node is None:
            self.node = Node(key)
            queue.pop()

        while len(queue) > 0:
            current = queue.pop(0)
            
            if key < current.node.key:
                if current.node.left is not None:
                    queue.append(current.node.left)
                else:
                    current.node.left = AVLTree(Node(key))
            elif key > current.node.key or key == current.node.key:
                if current.node.right is not None:
                    queue.append(current.node.right)
                else:
                    current.node.right = AVLTree(Node(key))

        self.rebalance()
