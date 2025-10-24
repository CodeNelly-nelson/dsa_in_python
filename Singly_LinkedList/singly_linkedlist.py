# LINKEDLIST

# Big O of LinkedLists Methods

# adding to end = O(1)
# Removing from end = O(n)

# Adding to the front = O(1)
# Removing from the front = O(1)

# Adding item at the middle = O(n)
# removing item at the middle = O(n)

# Searching for an element = O(n)


# --------inkedlist under the hood -----


head = {
    "value": 11,
    "next": {"value": 3, "next": {"value": 23, "next": {"value": 7, "next": None}}},
}

# print out value 23
# print(head["next"]["next"]["value"])


"""TODO: LinkedList"""


# class to create single node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# the class the construct a linkedlist
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Method to add an item to the end of the linkedlist O(1)
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True

    # Method to remove and return an item to the end of the linkedlist O(n)
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    # Method to add an item to the front or beginning of the linkedlist O(1)
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True

    # pop first item of from the beginning O(1)
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    # get an item by index
    def get_item(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # set the value of a Node in the linked list
    def set_value(self, index, value):
        temp = self.get_item(index)
        if temp:
            temp.value = value
            return True
        return False

    # insert and item a particular index
    def insert_at_index(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get_item(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    # Removing of a node  at an index
    def remove_at_index(self, index):
        # Check for invalid index
        if index < 0 or index >= self.length:
            return None
        # Remove the first node
        if index == 0:
            return self.pop_first()
        # Remove the last node
        if index == self.length - 1:
            return self.pop()
        # Remove a middle node
        prev = self.get_item(index - 1)  # Get the node before the one to remove
        temp = prev.next  # The node to remove
        prev.next = temp.next  # Skip over 'temp'
        temp.next = None  # Disconnect 'temp'
        self.length -= 1
        return temp

    def reverse_LL(self):
        # If the list is empty or has only one node, no need to reverse
        if not self.head or not self.head.next:
            return True
        # Swap head and tail first
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # Initialize pointers
        before = None
        after = None
        # Traverse the list and reverse the links
        for _ in range(self.length):
            after = temp.next  # store next node
            temp.next = before  # reverse the pointer
            before = temp  # move before forward
            temp = after  # move temp forward
        return True

    # method to print all linked list items
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(f" {temp.value} -> ", end="")
            temp = temp.next
        print("None")


""" Main Program entry"""


def main():

    my_linked_list = LinkedList(11)  # initialize the linked list with 11
    my_linked_list.append(4)
    my_linked_list.append(2)
    my_linked_list.append(8)

    print("Initial LinkedList: ", end="")
    my_linked_list.print_list()

    print("Head:", my_linked_list.head.value)  # get the head of the linked list
    print("Tail:", my_linked_list.tail.value)  # get the tail of the linked list
    print("Length:", my_linked_list.length)

    print("\n#****** After removing of a node  at an index *****#\n")

    my_linked_list.reverse_LL()

    print("Head:", my_linked_list.head.value)  # get the head of the linked list
    print("Tail:", my_linked_list.tail.value)  # get the tail of the linked list
    print("Length:", my_linked_list.length)

    print("LinkedList: ", end="")
    my_linked_list.print_list()


if __name__ == "__main__":
    main()
