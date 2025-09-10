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
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }    
}

# print out value 23
# print(head["next"]["next"]["value"])


"""TODO: LinkedList"""

# class to create single node
from os import pread
from more_itertools import tail
from textdistance import length


class Node:
    def __init__(self,value):
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
            self.tail.next  = new_node
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
        
    # method to print all linked list items
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(f" {temp.value} -> ", end="")
            temp = temp.next
        print("None")





""" Main Program entry"""

def main():
    
    my_linked_list = LinkedList(11)  # initialize the linked list with 4
    my_linked_list.append(3)   # add new node to the linked list\
    my_linked_list.append(23) 
    my_linked_list.append(7) 
    my_linked_list.append(4) 
    
    print("Initial LinkedList: ", end="" )
    my_linked_list.print_list() 
    
    # Adding to front
    my_linked_list.prepend(30)
   
    
    
    print("Head:", my_linked_list.head.value)   # get the head of the linked list
    print("Tail:", my_linked_list.tail.value)   # get the tail of the linked list
    print("Length:",my_linked_list.length)
    
    print("LinkedList: ", end="" )
    my_linked_list.print_list() 
    
    print("Popped item: ",my_linked_list.pop())
    # print("Popped item: ",my_linked_list.pop())
    # print("Popped item: ",my_linked_list.pop())
    # print("Popped item: ",my_linked_list.pop())
    # print("Popped item: ",my_linked_list.pop())

    
    print("\nAfter pops ")
     
    if my_linked_list.length == 0:
        print("Head:", my_linked_list.head)   # get the head of the linked list
        print("Tail:", my_linked_list.tail)   # get the tail of the linked list
        print("Length:",my_linked_list.length)
    else:
        print("Head:", my_linked_list.head.value)   # get the head of the linked list
        print("Tail:", my_linked_list.tail.value)   # get the tail of the linked list
        print("Length:",my_linked_list.length)
        
    print("LinkedList: ", end="" )
    my_linked_list.print_list()     # print all the elements of the linked list


    
if __name__ == "__main__":
    main()

