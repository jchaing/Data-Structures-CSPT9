class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

    def __str__(self):
        return f"Value: {self.value}, Next_Node: {self.next_node}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_length(self):
        return self.length

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:  # if self.head is None and self.tail is None
            self.tail = new_node
        self.length += 1
        print("ADD TO HEAD")
        print(f"Head: {self.head}")
        print(f"Tail: {self.tail}")
        print(f"Length: {self.length}")

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1
        print("ADD TO TAIL")
        print(f"Head: {self.head}")
        print(f"Tail: {self.tail}")
        print(f"Length: {self.length}")

    def remove_head(self):
        # empty LL
        if self.head is None:
            print("REMOVE HEAD")
            print(f"Head: {self.head}")
            print(f"Tail: {self.tail}")
            print(f"Length: {self.length}")
            return None
        # list with 1 node
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            print("REMOVE HEAD")
            print(f"Head: {self.head}")
            print(f"Tail: {self.tail}")
            print(f"Length: {self.length}")
            print(f"Removed head, {value}")
            return value
        # list with 2+ node
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            print("REMOVE HEAD")
            print(f"Head: {self.head}")
            print(f"Tail: {self.tail}")
            print(f"Length: {self.length}")
            print(f"Removed head, {value}")
            return value

    def remove_tail(self):
        # empty LL
        if self.tail is None:
            print("REMOVE TAIL")
            print(f"Head: {self.head}")
            print(f"Tail: {self.tail}")
            print(f"Length: {self.length}")
            return None
        # list with 1 node
        elif self.tail == self.head:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            print("REMOVE TAIL")
            print(f"Head: {self.head}")
            print(f"Tail: {self.tail}")
            print(f"Length: {self.length}")
            print(f"Removed tail, {value}")
            return value
        # list with 2+ node
        else:
            value = self.tail.get_value()
            curr_node = self.head
            prev_node = None
            while curr_node.next_node is not None:
                prev_node = curr_node
                curr_node = curr_node.get_next()
            prev_node.set_next(None)
            self.length -= 1
            print("REMOVE TAIL")
            print(f"Head: {self.head}")
            print(f"Tail: {self.tail}")
            print(f"Length: {self.length}")
            print(f"Removed tail, {value}")
            return value

    def contains(self, value):
        curr_node = self.head
        # check if value of current node is the Value
        while curr_node is not None:
            if value == curr_node.get_value():
                return True
            curr_node = curr_node.get_next()
        return False

    def get_max(self):
        # empty list
        if self.head is None:
            return None

        # non-empty list
        # iterate through all elements
        curr_node = self.head
        curr_max = self.head.get_value()
        while curr_node is not None:
            if curr_node.get_value() > curr_max:
                curr_max = curr_node.get_value()
            curr_node = curr_node.get_next()

        return curr_max


linked_list = LinkedList()

# linked_list.add_to_head(10)
# linked_list.add_to_head(11)
# linked_list.add_to_head(12)

# linked_list.add_to_tail(2)
# linked_list.add_to_tail(3)
# linked_list.add_to_tail(4)

# linked_list.add_to_head(20)
# linked_list.add_to_tail(40)
# linked_list.add_to_tail(60)
# linked_list.remove_head()

# linked_list.add_to_head(20)
# linked_list.add_to_head(40)
# linked_list.add_to_head(60)
# linked_list.remove_tail()

# linked_list.add_to_head(20)
# linked_list.add_to_tail(40)
# linked_list.add_to_tail(60)
# linked_list.contains()

# linked_list.add_to_head(20)
# linked_list.add_to_head(10)
# linked_list.contains(20)
