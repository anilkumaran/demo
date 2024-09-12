import heapq

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def enqueue(self, priority, item):
        heapq.heappush(self.pq, (priority, item))

    def dequeue(self):
        if len(self.pq) == 0:
            return None
        return heapq.heappop(self.pq)[1]

# Example usage:
hospital_queue = PriorityQueue()
hospital_queue.enqueue(2, 'Regular Checkup')
hospital_queue.enqueue(1, 'Emergency')
print(hospital_queue.dequeue())  # Output: Emergency because 1 is priority
