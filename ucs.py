from priority_queue import PriorityQueue

class UCSearch:
    def __init__(self, graph):
        self._graph = graph
        self._frontier = PriorityQueue()
        self._explored = {}

    def ucs(self, start, goal, verbose=True):
        node = start
        self._frontier.insert((0, node, []))
        while self._frontier:
            if(self._frontier.isEmpty()):
                print('\nNo Solution.')
                return None

            cost, node, path = self._frontier.pop()
            if node in self._explored and self._explored[node] < cost:
                continue

            # Create the path to the Solution
            path = path + [node]
            # Show the cumulative cost to get to a state, the current state and
            # the path that we took to get there.
            if verbose:
                print("Cost: {}, State: {}, Path: {}".format(cost, node, path))

            if node==goal:
                return path

            # Need to convert the networkx graph to a python dictionary. Makes my
            # life simpler.
            graphToDict = dict(self._graph[node])
            # Get the children nodes and their costs. The keys of the dictionary
            # are the names of the state and the val['weight'] are the costs.
            for key, vals in graphToDict.items():
                child_node = key
                child_cost = vals['weight']
                if child_node not in self._explored or child_node not in path:
                    self._frontier.insert((cost + child_cost, child_node, path))
            self._explored[node] = cost
