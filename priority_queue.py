import heapq

def isCostHigher(pq, key, cost):
    for c, k, _ in pq._queue:
        if key==k and cost > c:
            return True
        return False

def replace(pq, item):
    for i in range(len(pq._queue)):
        if pq._queue[i][1] == item[1]:
            del pq._queue[i]
            pq._queue.append(item)

class PriorityQueue(object):

    def __init__(self):
        self._queue = []

    def __str__(self):
        """Prints the contents of the priority queue. Enables the print function
        to work on the priority queue."""
        return ' '.join([str(i) for i in self._queue])

    def __contains__(self, key):
        """Enables the 'in' operator to work."""
        return key in [key for _, key, _ in self._queue]

    def insert(self, item):
        heapq.heappush(self._queue, item)

    def pop(self):
        return heapq.heappop(self._queue)

    def isEmpty(self):
        return len(self._queue) == 0

# Test
if __name__ == '__main__':
    pq = PriorityQueue()
    pq.insert((10, 'london', ['london']))
    node = 'aberdeen'
    print(node in pq) # False
    node = 'london'
    print(node in pq) # True
    print(pq)

    print("\nTesting isCostHigher()")
    child_node = 'london'
    child_cost = 100
    print(isCostHigher(pq, child_node, child_cost)) # True
    print("\nTesting replace()...")
    replace(pq, (child_cost, child_node, ['brighton', 'london']))
    print(pq)
