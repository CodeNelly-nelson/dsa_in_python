# TODO:  Find middle node

# Rules
# No length attribute
# Don't calculate the length of the list
# You cn only loop over the list one time



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        


    # Append a new node at the end
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Find middle node using two-pointer technique
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Helper to display list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")
        
        
        
        



# ============================
# 🔸 TEST 1: ODD number of nodes
ll_odd = LinkedList()
for val in [1, 2, 3, 4, 5]:
    ll_odd.append(val)
print("Odd List:")
ll_odd.print_list()
middle_odd = ll_odd.find_middle_node()
print("Middle Node (Odd):", middle_odd.value)   # Expected: 3

# ============================
# 🔸 TEST 2: EVEN number of nodes
ll_even = LinkedList()
for val in [10, 20, 30, 40, 50, 60]:
    ll_even.append(val)
print("\nEven List:")
ll_even.print_list()
middle_even = ll_even.find_middle_node()
print("Middle Node (Even):", middle_even.value)  # Expected: 40 (first of second half)

# ============================
# 🔸 TEST 3: SINGLE node
ll_single = LinkedList()
ll_single.append(99)
print("\nSingle Node List:")
ll_single.print_list()
middle_single = ll_single.find_middle_node()
print("Middle Node (Single):", middle_single.value)  # Expected: 99
