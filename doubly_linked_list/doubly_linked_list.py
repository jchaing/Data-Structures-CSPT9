"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


from typing import List


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __str__(self):
        return f"Value: {self.value}, Prev: {self.prev}"

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


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
        new_node = ListNode(value, next=self.head)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

        print("ADD TO HEAD")
        print(f"Head: {self.head}")
        print(f"Tail: {self.tail}")
        print(f"Length: {self.length}")

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            curr_head = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1

            print("REMOVE FROM HEAD")
            print(f"Head: {self.head}")
            print(f"Tail: {self.tail}")
            print(f"Length: {self.length}")
            print(f"Removed: {curr_head}")
            return curr_head
        else:
            curr_head = self.head.value
            self.head = self.head.next
            self.length -= 1

            print("REMOVE FROM HEAD")
            print(f"Head: {self.head}")
            print(f"Tail: {self.tail}")
            print(f"Length: {self.length}")
            print(f"Removed: {curr_head}")
            return curr_head

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value, next=self.tail)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        print("ADD TO TAIL")
        print(f"Head: {self.head}")
        print(f"Tail: {self.tail}")
        print(f"Length: {self.length}")
        return new_node

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.tail is None:
            return None
        elif self.tail == self.head:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            curr_tail = self.tail.value
            self.tail = self.tail.prev
            self.length -= 1

            print("REMOVE FROM TAIL")
            print(f"Head: {self.head}")
            print(f"Tail: {self.tail}")
            print(f"Length: {self.length}")
            print(f"Removed: {curr_tail}")
            return curr_tail


    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):

        # store node for use before removal
        curr_node = node.value

        # if node is the head, don't remove head
        if node == self.head:
            return

        # if node is tails
        elif node == self.tail:

            # remove tail and decrement
            self.remove_from_tail()

        # if node is not tail
        else:
            node.delete()
            self.length -= 1

        # add stored node value to head
        self.add_to_head(curr_node)


    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):

        # store node for use before removal
        curr_node = node.value

        # if node is the tail, don't remove tail
        if node == self.tail:
            return

        # if node is head
        if node == self.head:

            # remove head and decrement
            self.remove_from_head()

        # if node is not head
        else:

            # delete node
            node.delete()

            # decrement
            self.length -= 1

        # add node to tail
        self.add_to_tail(curr_node)


    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):

        # check if empty DLL
        if self.tail is None and self.head is None:
            return

        # decrement if not empty
        self.length -= 1

        # if DLL is only 1 node
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # if node is tail
        if self.tail == node:
            self.tail = self.tail.prev

        # if node is head
        elif self.head == node:
            self.head = self.head.next

        # remove node
        node.delete()
        # node.prev.next = node.next
        # node.next.prev = node.prev

        print(f"Head: {self.head}")
        print(f"Tail: {self.tail}")
        print(f"Length: {self.length}")


    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """

    def get_max(self):
        # handle empty list
        if self.head is None:
            return None

        # keep track of current max
        curr_node = self.head
        curr_max = self.head.value

        # loop through
        while curr_node is not None:
            if curr_node.value > curr_max:
                curr_max = curr_node.value
            curr_node = curr_node.next

        print(f"Current Max: {curr_max}")
        # return max
        return curr_max


# dll = DoublyLinkedList()

# dll.add_to_head(20)
# dll.add_to_head(40)

# dll.add_to_head(20)
# dll.add_to_head(40)
# dll.remove_from_head()

# dll.add_to_head(20)
# dll.add_to_head(40)
# dll.add_to_tail(60)

# dll.add_to_head(20)
# dll.add_to_head(40)
# dll.remove_from_tail()

# dll.add_to_head(20)
# dll.add_to_head(40)
# dll.delete(dll.tail)

# dll.add_to_head(20)
# dll.add_to_head(40)
# dll.add_to_head(60)
# dll.add_to_head(80)
# dll.get_max()

# dll.add_to_head(20)
# dll.add_to_head(40)
# dll.add_to_head(60)
# dll.add_to_head(80)
# dll.move_to_front(dll.tail)

# dll.add_to_head(20)
# dll.add_to_head(40)
# dll.add_to_head(60)
# dll.add_to_head(80)
# dll.move_to_end(dll.head)
