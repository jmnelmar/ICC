class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]
        return None
    
    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return bool(self.items)
    
    def to_list(self):
        return self.items
    
    def __str__(self):
        stack_string = ""
        for i in reversed(self.items):
            stack_string += f"({i})\n"
            stack_string += f"===\n"
        return stack_string