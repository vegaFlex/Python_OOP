class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        # return bool(self.data)
        return len(self.data) == 0

    def __str__(self):
        # return ", ".join([str(el) for el in self.data[::-1]])
        return "[" + ", ".join(reversed(self.data)) + "]"


stack = Stack()
stack.is_empty()
stack.push("a")
stack.push('b')
stack.push('c')
print(stack.top())
stack.pop()
print(stack)
