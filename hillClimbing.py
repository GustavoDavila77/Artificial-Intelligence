from abc import ABCMeta
from math import exp
from random import randint, uniform
import random
from urllib.request import randombytes
from aima.core import search
from aima.core.search import utils
from aima.core.search.framework import NodeExpander, Node
from aima.core.util.other import PlusInfinity

__author__ = 'Ivan Mushketik'
__docformat__ = 'restructuredtext en'

 # Artificial Intelligence A Modern Approach (3rd Edition): Figure 4.2, page 122.
 #
 # function HILL-CLIMBING(problem) returns a state that is a local maximum
 #
 #   current <- MAKE-NODE(problem.INITIAL-STATE)
 #   loop do
 #     neighbor <- a highest-valued successor of current
 #     if neighbor.VALUE <= current.VALUE then return current.STATE
 #     current <- neighbor
 #
class HillClimbingSearch(NodeExpander):
    """
    The most basic algorithm of local search. At each state al reachable states from the current one are expanded. Current
    state is substituted by a state with the best heuristic estimation (if one exists). If all expanded states' heuristic
    estimation is worse that the current state's estimation, the search is over.
    """
    def __init__(self, heuristic_function):
        super().__init__()
        self.heuristic_function = heuristic_function

    def is_failure(self):
        return self.failure != False

    # function HILL-CLIMBING(problem) returns a state that is a local maximum
    def search(self, problem):
        self.clear_instrumentation()

        self.failure = True
        self.last_state = None
        # current <- MAKE-NODE(problem.INITIAL-STATE)
        current_node = Node(problem.get_initial_state())

        while True:
            children = self.expand_node(current_node, problem)
            # neighbor <- a highest-valued successor of current
            neighbor = self._get_lowest_valued_node(children)
            
            # if neighbor.VALUE <= current.VALUE then return current.STATE
            if neighbor == None or self._get_value(current_node) <= self._get_value(neighbor):
                if search.utils.is_goal_state(problem, current_node):
                    self.failure = False
                self.last_state = current_node.get_state()
                return search.utils.actions_from_nodes(current_node.get_path_from_root())

            # current <- neighbor
            current_node = neighbor

    def _get_lowest_valued_node(self, children):
        """
        Get node with the lowest (the best) estimation of heuristic function
        :param children: children of current node
        :return: node with the best heuristic estimation
        """
        lowest_value = PlusInfinity()
        node_with_lowest_value = None

        for node in children:
            value = self._get_value(node)
            if value < lowest_value:
                node_with_lowest_value = node
                lowest_value = value

        return node_with_lowest_value

    def _get_value(self, node):
        return self.heuristic_function.h(node.get_state())


class Scheduler:
    def __init__(self, k=20, lam=0.045, limit=100):
        self.k = k
        self.lam = lam
        self.limit = limit

    def get_temp(self, time):
        if time < self.limit:
            return self.k * exp(-1 * self.lam * time)
        else:
            return 0


def main():
    nodes = [1, 2, 3, 4, 5, 6, 7]
    world = pants.World(nodes, length_function)
    solver = pants.Solver()
    solution = solver.solve(world)
    print(solution.distance)
    print(solution.tour)    # Nodes visited in order
    #print(solution.path)    # Edges taken in order


if __name__ == '__main__':
    main()

"""
def hill_climbing(problem, iterations_limit=0, viewer=None):
    '''
    Hill climbing search.

    If iterations_limit is specified, the algorithm will end after that
    number of iterations. Else, it will continue until it can't find a
    better node than the current one.
    Requires: SearchProblem.actions, SearchProblem.result, and
    SearchProblem.value.
    '''
    return _local_search(problem,
                         _first_expander,
                         iterations_limit=iterations_limit,
                         fringe_size=1,
                         stop_when_no_better=True,
                         viewer=viewer)
"""