"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        elif value > self.value or value == self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False

        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        
        if self.left is not None:
            self.left.for_each(fn)

        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return

        if node.left is not None:
            node.in_order_print(node.left)

        print(f"{node.value}")

        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None:
            return
        
        queue = []
        queue.append(node)

        while(len(queue) > 0):
            print(f"{queue[0].value}")

            current = queue.pop(0)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node is None:
            return
        
        stack = []
        stack.append(node)

        while(len(stack) > 0):

            current = stack.pop()
            print(f"{current.value}")

            if current.right is not None:
                stack.append(current.right)
                
            if current.left is not None:
                stack.append(current.left)

            
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node is None:
            return

        print(f"{node.value}")

        if node.left is not None:
            node.pre_order_dft(node.left)

        if node.right is not None:
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is None:
            return

        if node.left is not None:
            node.post_order_dft(node.left)

        if node.right is not None:
            node.post_order_dft(node.right)
        
        print(f"{node.value}")
