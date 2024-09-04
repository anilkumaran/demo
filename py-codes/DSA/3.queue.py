from collections import deque


class Queue:
    def __init__(self) -> None:
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft() if len(self.queue) else None
    
    def count(self, item):
        return self.queue.count(item)

        
# Example usage:
task_queue = Queue()
task_queue.enqueue('Task 1')
task_queue.enqueue('Task 2')
task_queue.enqueue(1)
task_queue.enqueue(2)
task_queue.enqueue(3)
task_queue.enqueue(1)
print(task_queue.count(1))  # Output: Task 1
# print(task_queue.dequeue())  # Output: Task 1
