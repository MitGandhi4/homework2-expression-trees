class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
            """
            Push an item onto the top of the stack.
            """
            self.items.append(item)