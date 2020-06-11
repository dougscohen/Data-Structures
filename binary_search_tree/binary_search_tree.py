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
        # compare the value to root's value to determine which direction
        # . to go
        # if value < root
        if value < self.value:
            # go left
            # Check if there is a left node already
            if self.left:
                # if there is, run insert on self.left
                self.left.insert(value)
            else:
                # then we can park the value here
                self.left = BSTNode(value)
        # else value >= root
        else:
            # go right
            # Check if there is a right node already
            if self.right:
                # if there is, run insert on self.right
                self.right.insert(value)
            else:
                # no right node and we can park the value here
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check to see if the root is the target
        if self.value == target:
            return True
        # Otherwise, there is a root Node but it isn't the target, thus we to
        # . go left or right
        else:
            # if target < root, go left
            if target < self.value:
                # Check to see if there is a left node already
                if self.left:
                    # if there is, run contains (recur) on self.left
                    return self.left.contains(target)

            else:
                # Check to see if there is a right node already
                if self.right:
                    # if there is, run contains (recur) on self.right
                    return self.right.contains(target)

            # if there is no left or right node and target hasn't been found
            #. yet, return False
            return False
    
    
    # Return the maximum value found in the tree

    def get_max(self):
        # Check to see if there is a right node. If there isn't, return the
        #. value
        if not self.right:
            return self.value
        # Otherwise: recur on right side
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Call the function 'fn' on the current value
        fn(self.value)
        # Check to see if there is a left node
        if self.left:
            # if there is, make the left node the current value
            self.left.for_each(fn)
        # Check to see if there is a right node
        if self.right:
            # if there is, make the right node the current value
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):

        if node:
            # recur on left child of the node
            node.in_order_print(node.left)
            # print the value of the left child
            print(node.value)
            # recur on right child of the node
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):

        if node:
            # Print the value of the root
            print(node.value)
            # Recur on left child
            node.pre_order_dft(node.left)
            # Recur on right child
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):

        if node:
            # Recur on the left child
            node.post_order_dft(node.left)
            # Recur on the right child
            node.post_order_dft(node.right)
            # Print the root
            print(node.value)
