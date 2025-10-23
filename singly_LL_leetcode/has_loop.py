class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
        
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
        
        
        # helper function to print
    def print_linkedlist(self):
        temp = self.head            
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")
        

## Has loop
my_linked_list_1 = LinkedList(4)
my_linked_list_1.append(10)
my_linked_list_1.append(5)
my_linked_list_1.print_linkedlist()
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop())
print(my_linked_list_1.head.value)
print(my_linked_list_1.tail.next.value)


## Has no loop
my_linked_list_1 = LinkedList(4)
my_linked_list_1.append(10)
my_linked_list_1.append(5)
my_linked_list_1.print_linkedlist()
print(my_linked_list_1.has_loop())
print(my_linked_list_1.head.value)
print(my_linked_list_1.tail.value)
