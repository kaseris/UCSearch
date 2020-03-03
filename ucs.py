from priority_queue import *

class UCSearch:
    def __init__(self, graph, optimisation_att='weight'):
        self._graph = graph
        self._frontier = PriorityQueue()
        self._explored = {}
        self._opt_att = optimisation_att
        print("Created a new UCS pathfinder optimising for: {}".format(self._opt_att))

    def ucs(self, start, goal, verbose=True):
        node = start
        self._frontier.insert((0, node, 0.0, []))
        while self._frontier:
            if(self._frontier.isEmpty()):
                print('\nNo Solution.')
                return None

            cost, node, time, path = self._frontier.pop()
            if node in self._explored and self._explored[node] < cost:
                continue

            # Create the path to the Solution
            path = path + [node]
            # Show the cumulative cost to get to a state, the current state and
            # the path that we took to get there.
            if verbose:
                print("\nCost: {}, State: {}, Time: {}, Path: {}".format(cost, node, time, path))
                print("Explored: {}".format(list(self._explored.keys())))
                print("Frontier: {}".format(self._frontier))
            if node==goal:
                print("\nSolution Found!")
                return path

            # Need to convert the networkx graph to a python dictionary. Makes my
            # life simpler.
            graphToDict = dict(self._graph[node])
            # Get the children nodes and their costs. The keys of the dictionary
            # are the names of the state and the val['self._opt_att'] are the costs.
            for key, vals in graphToDict.items():
                child_node = key
                child_cost = vals[self._opt_att]
                if 'time' in graphToDict.items():
                    child_time = vals['time']
                else:
                    child_time = 0.0
                if child_node not in self._explored or child_node not in self._frontier:
                    self._frontier.insert((cost + child_cost, child_node, time + child_time, path))
                elif child_node in self._frontier and isCostHigher(self._frontier, child_node, child_cost):
                    replace(self._frontier, (cost + child_cost, child_node, time + child_time, path))
            self._explored[node] = cost
