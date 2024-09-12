import heapq

# Min heap
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
print(heapq.heappop(heap))  # Output: 1

# Max heap
max_heap = []
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -5)
print(-heapq.heappop(max_heap))  # Output: 10
