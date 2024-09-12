class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if len(self.stack) else None

    def peek(self):
        return self.stack[-1] if len(self.stack) else None
    

browser_history = Stack()
browser_history.push('www.google.com')

browser_history.push('www.github.com')
print(browser_history.pop())
