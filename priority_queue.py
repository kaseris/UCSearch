import heapq

class PriorityQueue(object):

    def __init__(self):
        self._queue = []

    def __str__(self):
        """Prints the contents of the priority queue. Enables the print function
        to work on the priority queue."""
        return ' '.join([str(i) for i in self._queue])

    def __contains__(self, key):
        """Enables the 'in' operator to work."""
        return key in [key for key, _, _ in self._queue]

    def insert(self, item):
        heapq.heappush(self._queue, item)

    def pop(self):
        return heapq.heappop(self._queue)

    def isEmpty(self):
        return len(self._queue) == 0

# Test
if __name__ == '__main__':
    pq = PriorityQueue()
    pq.insert(('london', 0, ['london']))
    node = 'aberdeen'
    print(node in pq) # False
    node = 'london'
    print(node in pq) # True
    print(pq)
