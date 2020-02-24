import heapq

class PriorityQueue(object):

    def __init__(self):
        self._queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self._queue])

    def insert(self, priority, item):
        heapq.heappush(self._queue, (priority, item))

    def pop(self):
        return heapq.heappop(self._queue)

    def isEmpty(self):
        return len(self._queue) == 0


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.insert(0, 'london')
    pq.insert(100, 'birmingham')
    pq.insert(40, 'brighton')
    pq.insert(50, 'oxford')
    pq.insert(60, 'cambridge')
    print(pq)
    while(not pq.isEmpty()):
        print(pq.pop())
