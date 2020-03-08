import heapq
# Change this to cost < c
def isCostHigher(pq, key, cost):
    for c, k, _, _ in pq._queue:
        if key==k and cost < c:
            return True
        return False

def replace(pq, item):
    count = 0
    for i in range(len(pq._queue)):
        if pq._queue[i][1] == item[1] and item[0] < pq._queue[i][0]:
            pq._queue[i] = (-1, item[1], item[2], item[3])
            count += 1
    heapq.heapify(pq._queue)

    for i in range(count):
        pq.pop()

    pq.insert(item)

class PriorityQueue(object):

    def __init__(self):
        self._queue = []

    def __str__(self):
        """Prints the contents of the priority queue. Enables the print function
        to work on the priority queue."""
        return ' '.join([str(i) for i in self._queue])

    def __contains__(self, key):
        """Enables the 'in' operator to work."""
        return key in [key for _, key, _, _ in self._queue]

    def insert(self, item):
        heapq.heappush(self._queue, item)

    def pop(self):
        return heapq.heappop(self._queue)

    def isEmpty(self):
        return len(self._queue) == 0

# Test
if __name__ == '__main__':
    # pq = PriorityQueue()
    # pq.insert((10, 'london', ['london']))
    # node = 'aberdeen'
    # print(node in pq) # False
    # node = 'london'
    # print(node in pq) # True
    # print(pq)
    #
    # print("\nTesting isCostHigher()")
    # child_node = 'london'
    # child_cost = 100
    # print(isCostHigher(pq, child_node, child_cost)) # True
    # print("\nTesting replace()...")
    # replace(pq, (child_cost, child_node, ['brighton', 'london']))
    # print(pq)
    #
    # print("\nTesting the statement")
    # if isCostHigher(pq, child_node, child_cost):
    #     replace(pq, (child_cost, child_node, ['brighton', 'london']))
    # print(pq)

    pq2 = PriorityQueue()
    pq2.insert((5, 'wow', 0.0, []))
    pq2.insert((4, 'wow', 0.0, []))
    pq2.insert((32, 'nikos', 0.0, ['asdad']))
    pq2.insert((7, 'wow', 0.0, []))
    pq2.insert((8, 'trakis', 0.0, ['asdasd']))
    pq2.insert((849, 'wow', 0.0, ['asd']))
    print("Test the replace")
    item = (2, 'wow', 0.0, ['asdasdas'])
    child = 'trakis'
    print("IS IN FRONTIER: {}".format(child in pq2))
    print("IS COST HIGHER IN FRONTIER: {}".format(isCostHigher(pq2, 'wow', 2)))
    aDict = {'bekos': 0, 'wow': 2, 'trakis': 20}
    print("IS THE NODE IN THE DICT? {}".format(child in aDict))
    if child in pq2 and isCostHigher(pq2, 'wow', 2):
        replace(pq2, (2 + 1, 'wow', 0.0, ['hey']))

    while not pq2.isEmpty():
        print(pq2.pop())
