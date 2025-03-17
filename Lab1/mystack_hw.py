class MyStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
  
    def __init__(self):
        """Create an empty stack."""
        self._data = []             
  
    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)
  
    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0
  
    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)
  
    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[-1]
               
    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data.pop()


def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    S = MyStack()  
    with open(filename, 'r') as file:  
        for line in file:
            S.push(line.rstrip())
    
    with open(filename, 'w') as file:  
        while not S.is_empty():
            file.write(S.pop() + '\n')

def test_stack():
    """ test the stack"""
    stack = MyStack()
    print("Stack empty?:", stack.is_empty())   #True
    stack.push(5)
    stack.push(15)
    stack.push(55)
    print("Current top element:", stack.top())  
    print("Popping element:", stack.pop())  
    print("Check stack size:", len(stack))  
    print("Stack empty?:", stack.is_empty())  #False

    print("Testing edge cases...")
    stack.push(100)
    stack.push(200)
    print("New top after pushes:", stack.top())
    print("Popping all elements...")
    print(stack.pop(), stack.pop(), stack.pop(), stack.pop())
    print("Stack empty after popping all elements?", stack.is_empty())
    
    print("Testing pop on empty stack (should raise error)")
    try:
        stack.pop()
    except IndexError as e:
        print("Caught error as expected:", e)
    
    print("Testing top on empty stack (should raise error)")
    try:
        stack.top()
    except IndexError as e:
        print("Caught error as expected:", e)

    print("Testing pushing and popping multiple elements")
    for i in range(10):
        stack.push(i)
    while not stack.is_empty():
        print("Popped:", stack.pop())
    

if __name__ == "__main__":
    filename = "file.txt"
    test_stack()
    reverse_file(filename)
