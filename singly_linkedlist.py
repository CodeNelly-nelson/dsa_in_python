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


from doctest import FAIL_FAST


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
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get_item(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

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

    print("Node removed: ", my_linked_list.remove_at_index(1))

    print("Head:", my_linked_list.head.value)  # get the head of the linked list
    print("Tail:", my_linked_list.tail.value)  # get the tail of the linked list
    print("Length:", my_linked_list.length)

    print("LinkedList: ", end="")
    my_linked_list.print_list()


if __name__ == "__main__":
    main()
