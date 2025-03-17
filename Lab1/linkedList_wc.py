# Node class to be a part of Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a class called LinkedList 
class LinkedList:
    def __init__(self):
        self.head = None

    # Add a node at the begining
    def add_first(self, data):
        """ Add Firdt Node"""
        if self.head == None:
            ll=Node(data)
            self.head=ll
        else:
            ll=Node(data)
            c1=self.head
            self.head=ll
            self.head.next = c1

    ### Insert at the end
    def add_last(self, data):
        """Add node at last position."""
    # If the list is empty, the new node becomes head
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)

    def add_at_index(self, data,newdata):
        """Add node at a specifiec newdata"""
        c1=self.head
        dflag=False
        while c1:
            if c1.data == data:
              nn=Node(newdata)
              nn.next=c1.next
              c1.next=nn
              dflag=True
              break
            c1=c1.next
        if not dflag:
            print("No matching data found")
            
    def print_linked_list(self):
        """ print the  linked list"""
        currNode=self.head

        if currNode is not None:
            while currNode is not None:
                print(currNode.data)
                currNode=currNode.next

        '''
        if self.head is not None:
            while self.head is not None:
                print(self.head.data)
                self.head=self.head.next 
        '''

    def linked_size(self):
        """ Get the size of linked list"""
        len=0
        c1=self.head
        while c1.next is not None:
            len=len+1
            c1=c1.next
            
        print(len)

    def delete_node(self,data):
        """ delete the linked linked list node"""
        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
            # print(f"Traversing, current node: {current.data if current else 'None'}")
        
        if current is None:
            print("Node not found")
            # print("Node not found, returning")
            return
        
        if prev is None:
            self.head = current.next
            # print(f"Head node deleted, new head: {self.head.data if self.head else 'None'}")
        else:
            prev.next = current.next
            # print(f"Node with data {data} deleted")

    def delete_first_node(self):
        """ delete the linked linked list first node"""
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
      
    def delete_last_node(self):
        """ delete the linked linked list last node"""
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def delete_at_index(self,data):
        """ delete the linked linked list node"""
        # Base Cases
        if not isinstance(data, int) or data < 0:
            print("Invalid index")
            return
        if self.head is None:
            print("List is empty")
            # print("List is empty, returning")
            return
        
        if data == 0:
            self.head = self.head.next
            # print(f"Node at index 0 deleted, new head: {self.head.data if self.head else 'None'}")
            return
        
        current = self.head
        prev = None
        for i in range(data):
            if current is None:
                print("Index out of bounds")
                # print("Index out of bounds during traversal")
                return
            prev = current
            current = current.next
            # print(f"Traversing, current node: {current.data if current else 'None'}")
        
        if current is None:
            print("Index out of bounds")
            return
        prev.next = current.next
        # print(f"Node at index {data} deleted")
    
    def reverse(self):
        """ This function reverse the list"""
         # Note: I tried doing this recursively in a unique way from before so I don't get accused of plagiarism again. Took some debugging but I eventually got it!
        if not self.head:
            return  # No need to reverse if the list is empty
        def reverse_recursive(current, prev):
            if not current:
                return prev
            next_node = current.next
            current.next = prev
            return reverse_recursive(next_node, current)

        self.head = reverse_recursive(self.head, None)


def linkedList():
    ll=LinkedList()
    ll.add_first(4)
    ll.add_first(5)
    ll.add_first(7)
    ll.add_first(8)
    ll.add_first(9)
    ll.add_last(20)
    ll.add_at_index(4,21)
    #ll.add_at_index(11,3)
    print("Linked List 1st time")
    ll.print_linked_list()
    print("Linked List 2nd time")
    ll.print_linked_list()
    ll.linked_size()

if __name__ == "__main__":
    linkedList()
    
    #Testing other functions
    ll = LinkedList()
    ll.add_first(10)
    ll.add_first(7)
    ll.add_first(8)
    ll.add_first(5)
    ll.add_first(9)
    
    print("Original Linked List:")
    ll.print_linked_list()
    
    print("\nReversing Linked List:")
    ll.reverse()
    ll.print_linked_list()
    
    print("\nDeleting node with value 7:")
    ll.delete_node(7)
    ll.print_linked_list()
    
    print("\nDeleting first node:")
    ll.delete_first_node()
    ll.print_linked_list()
    
    print("\nDeleting last node:")
    ll.delete_last_node()
    ll.print_linked_list()
    
    print("\nDeleting node at index 1:")
    ll.delete_at_index(1)
    ll.print_linked_list()



