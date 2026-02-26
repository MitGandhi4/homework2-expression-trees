class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
            """
            Push an item onto the top of the stack.
            """
            self.items.append(item)

    def pop(self):
        """
        Remove and return the top item of the stack.
        Raises an error if the stack is empty.
        """
        if len(self.items) == 0:
            raise IndexError("Pop from empty stack")

        return self.items.pop()
    def peek(self):
        """
        Return the top item of the stack without removing it.
        Raises an error if the stack is empty.
        """
        if len(self.items) == 0:
            raise IndexError("Peek from empty stack")

        return self.items[-1]

    def is_empty(self):
        """
        Return True if the stack is empty, otherwise False.
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the number of elements in the stack.
        """
        return len(self.items)