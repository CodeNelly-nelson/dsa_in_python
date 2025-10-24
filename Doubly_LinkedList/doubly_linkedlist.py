class Node:
    def __init__(self,value):
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
    def append(self,value):
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
        if self.tail is None:
            return None
        else:
            node_to_pop = self.tail
            self.tail = self.tail.prev
            node_to_pop.prev = None
            self.tail.next = None
        self.length -= 1
        return node_to_pop.value
        
        
            
            
            
            
    
            
            
    # method to print all linked list items
    def print_dll(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.value} -> ", end="")
            temp = temp.next
        print("None")
        
            
    
        
        



my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(8)
my_doubly_linked_list.append(4)


print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length)
my_doubly_linked_list.print_dll()
print(my_doubly_linked_list.pop())

