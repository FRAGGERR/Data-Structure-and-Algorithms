
class mystack:
    def __init__(self):
        self.s = []
    
    def push(self, x):
        self.s.append(x)
    
    def pop(self):
        if self.isnull():
            print("Error: Cannot pop from an empty stack")
            return None
        return self.s.pop()

    def size(self):
        return len(self.s)

    def isnull(self):
        return len(self.s) == 0
    
    def peek(self):
        if self.isnull():
            print("Error: Cannot pop from an empty stack")
            return None
        return self.s[-1]

    def print_stack(self):
        print(self.s)
        
if __name__ == '__main__':
    stack = mystack()
    print(stack.pop())        # Expected Output: 80
    print(stack.peek())       # Expected Output: 89
    print(stack.isnull())   # Expected Output: False
    print(stack.size())       # Expected Output: 3
    stack.print_stack()       # Expected Output: [5, 7, 89]

    # Attempt to pop all elements and one extra to trigger the error
    stack.pop()               # Expected Output: 89
    stack.pop()               # Expected Output: 7
    stack.pop()               # Expected Output: 5
    print(stack.pop())        # Expected Output: Error message and None
