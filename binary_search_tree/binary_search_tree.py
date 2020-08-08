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

import sys

sys.path.append('../queue/')

from queue import Queue


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"Value: {self.value}, Left: {self.left}, Right: {self.right}"

    # Insert the given value into the tree
    def insert(self, value):
        # capture current node value
        curr_node = self.value

        # start at root and loop until 'curr_node' is None
        if curr_node:
            if value <= curr_node:
                if self.left is None:
                    self.left = BSTNode(value)
                else:
                    self.left.insert(value)
            elif value > curr_node:
                if self.right is None:
                    self.right = BSTNode(value)
                else:
                    self.right.insert(value)
        else:
            curr_node = value
        return curr_node

    # Return True if the tree contains the value, else False
    # False if it does not
    def contains(self, target):

        # compare target_value to curr_value
        # 1. == we return True
        if target == self.value:
            return True

        # 2. < we go left
        elif target < self.value:

            # check if can't go left
            if self.left is None:
                return False

            # recursion
            else:
                return self.left.contains(target)

        # 3. > we go right
        elif target > self.value:

            # check if can't go right
            if self.right is None:
                return False

            # recursion
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):

        # check if root node exist
        if not self.value:
            return

        # capture current max
        curr_max = self.value

        # if no node to the right, return current max
        if self.right is None:
            return curr_max

        # if right node exists, recurse get_max() with right value
        elif self.right.value > self.value:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # 1. Base case - no more nodes in our subtree
        # 2. Recursive case

        fn(self.value)
        if self.left is not None:  # if self.left:
            self.left.for_each(fn)
        if self.right is not None:  # if self.right:
            self.right.for_each(fn)

        # # iterative method
        # curr_node = self
        # fn(curr_node.value)
        # stack =  # nodes you need to backtrack to
        # while curr_node.left:
        #     curr_node = curr_node.left
        #     fn(curr_node)
        #     # add it to the stack
        # # pop off the stack
        # # try to go right


    # STRETCH
    def delete(self, value):
        # search like we did in 'contains()'

        # different cases
        # if node at bottom level
            # update parent left/right = None
        #if node has only one child
            # parent.left/right = node.left/right
        #if node has two children
            # "larger" child becomes the parent of its sibling
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self:

            if self.left:
                # go left with recursion!
                self.left.in_order_print()
            print(self.value)
            if self.right:
                # go right wtih recursion!
                self.right.in_order_print()


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # use a queue
        # print current node, add left_child to queue, add right_child to queue
        # (if not None)
        # done when queue is empty
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # Left, Root, Right
    def dft_print(self):
        # create a stack
        stack = []
        # push some initial value(s)? onto the stack
        stack.append(self)
        # while stack is not empty
        while len(stack) > 0:
            # pop Node off top of stack to traverse its L&R Children
            current = stack.pop()

            # print current value
            print(current.value)

            # push ???
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        # done when stack is empty


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)
# print(f"bst {bst}")

bst.insert(8)
# print(f"bst {bst}")
bst.insert(5)
# print(f"bst {bst}")
bst.insert(7)
# print(f"bst {bst}")
bst.insert(6)
# print(f"bst {bst}")
bst.insert(3)
# print(f"bst {bst}")
bst.insert(4)
# print(f"bst {bst}")
bst.insert(2)
# print(f"bst {bst}")

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()

# print(bst.contains(33))
# print(bst.contains(3))
# print(bst.contains(7))
# print(bst.contains(100))

# print(bst.get_max())
