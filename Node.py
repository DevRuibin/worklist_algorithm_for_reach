from typing import List


class Node:
    """
    A node in the graph or a basic block in the control flow graph.
    It contains the following attributes:
    1. identifier: the name of the node
    2. data: the variables defined in the node
    3. parent: the parent nodes of the node
    4. children: the children nodes of the node
    5. reach_out: the reach out set of the node
    6. reach_in: the reach in set of the node

    Users don't need to care about the suffix of the variables. Like x is modified in Block A, so x_A is in the reach out.
    The suffix is added automatically.

    There are many methods so the size of the class is a little big. But it's easy to understands. This encapsulating
    is not recommended as it is only a simple demo, so please forgive me. I was sucked in the suffix problem, so I
    encapsulated many methods to make it easier to use, but it is not necessary and not recommended.
    """
    def __init__(self, identifier: str, definition: List[str]):
        """

        :param identifier: the name of the node
        :param definition: the variables defined in the node
        """
        self.__identifier = identifier
        self.__data = definition
        self.__parent = []
        self.__children = []
        self.__reach_out = set()
        self.__reach_in = set()

    def reach_in(self):
        return self.__reach_in

    def reach_out(self):
        return self.__reach_out

    def gen(self):
        gens = set()
        for item in self.__data:
            gens.add(item + "_" + self.__identifier)
        return gens

    def kill(self):
        kills = set()
        for item in self.__reach_in:
            name = item.split("_")[0]
            if name in self.__data:
                kills.add(item)
        return kills

    def set_parent(self, parent):
        self.__parent += parent

    def set_children(self, children):
        self.__children += children

    def add_reach_out(self, reach_out: set):
        self.__reach_out = self.__reach_out.union(reach_out)

    def add_reach_in(self, reach_in: set):
        self.__reach_in = self.__reach_in.union(reach_in)

    def set_reach_out(self, reach_out: set):
        self.__reach_out = reach_out

    def set_reach_in(self, reach_in: set):
        self.__reach_in = reach_in

    def get_parent(self):
        return self.__parent

    def get_children(self):
        return self.__children

    def get_identifier(self):
        return self.__identifier

    def get_data(self):
        return self.__data

    def __str__(self):
        return self.__identifier + ": " + str(self.__data)