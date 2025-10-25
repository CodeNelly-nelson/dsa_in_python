class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Append to a doubly linkedlist
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # Pop from a doubly linkedlist
    def pop(self):
        if self.length == 0:
            return None
        node_to_pop = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            node_to_pop.prev = None
        self.length -= 1
        return node_to_pop
    
    # Prepend a new node
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
        
    
        

    # method to print all linked list items
    def print_dll(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.value} -> ", end="")
            temp = temp.next
        print("None")

    # helper function to simulate edge case of empty dll
    def empty_ddl(self):
        self.head = None
        self.tail = None
        self.length = 0
        print("List emptied")


my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(8)
# my_doubly_linked_list.empty_ddl()


print()
print("Before prepend: ")
print("-" * 40)
print("Doubly LinkedList: ", end="")
my_doubly_linked_list.print_dll()
print("Head:", my_doubly_linked_list.head.value)
print("Tail:", my_doubly_linked_list.tail.value)
print("Length:", my_doubly_linked_list.length) 

my_doubly_linked_list.prepend(90)

print()
print("After prepend: ")
print("-" * 40)
print("Doubly LinkedList: ", end="")
my_doubly_linked_list.print_dll()
print("Head:", my_doubly_linked_list.head.value)
print("Tail:", my_doubly_linked_list.tail.value)
print("Length:", my_doubly_linked_list.length)
