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

    def __str__(self):
        return f"Value: {self.value}, Left: {self.left}, Right: {self.right}"

    # Insert the given value into the tree
    def insert(self, value):
        curr_node = self.value
        # print(f"curr_node: {curr_node}")
        # start at root and loop until 'curr_node' is None
        if self.value:
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
            self.value = value
        return curr_node

            # if 'value' <= 'curr_node'
                # if 'curr_node'.left is None
                    # insert our value!
                # else
                    # go left (update 'curr_node' to be 'curr_node.left')
            # elif 'value' > 'curr_node'
                # if 'curr_node.right' is None
                    # insert our value!
                # else
                    # go right (update 'curr_node' to be 'curr_node.right')


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare target_value to curr_value
            # 1. == we return True
            # 2. < we go left
            # 3. > we go right
            # 4. if can't go left/right (not found, return false)
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # go right!
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # STRETCH
    def delete(self, value):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

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
print(f"bst {bst}")

bst.insert(8)
print(f"bst {bst}")
bst.insert(5)
print(f"bst {bst}")
bst.insert(7)
print(f"bst {bst}")
bst.insert(6)
print(f"bst {bst}")
bst.insert(3)
print(f"bst {bst}")
bst.insert(4)
print(f"bst {bst}")
bst.insert(2)
print(f"bst {bst}")

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
