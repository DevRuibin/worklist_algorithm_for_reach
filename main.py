from typing import List
from Node import Node


def work_list_algorithm(nodes: List[Node]):
    while len(nodes) != 0:
        n = nodes.pop(0)
        old_reach_out = n.reach_out()
        n.set_reach_in(set())
        for parent in n.get_parent():
            n.add_reach_in(parent.reach_out())
        reach_out_set = n.gen().union(n.reach_in().difference(n.kill()))
        n.set_reach_out(reach_out_set)
        if old_reach_out != n.reach_out():
            for child in n.get_children():
                nodes.append(child)
    print("Work list algorithm finished!")


def make_graph():
    """
    Make a graph.
    Users can change the method according to their own needs, such as reading from a file.
    Just make sure that the nodes are connected correctly.
    :return: a list of nodes
    """
    A = Node("A", ["x", "y", "tmp"])
    B = Node("B", [])
    C = Node("C", ["tmp"])
    D = Node("D", ["x"])
    E = Node("E", ["y"])
    F = Node("F", [])

    A.set_children([B])
    B.set_children([C, F])
    C.set_children([D])
    D.set_children([E])
    E.set_children([B])
    F.set_children([])
    A.set_parent([])
    B.set_parent([A, E])
    C.set_parent([B])
    D.set_parent([C])
    E.set_parent([D])
    F.set_parent([B])
    return [A, B, C, D, E, F]


if __name__ == '__main__':
    """
    Example program: 
        public class GCD {
            public int gcd(int x, int y) {
            int tmp;                  // A: def x, y, tmp
            while (y != 0) {          // B: use y
                tmp = x % y;          // C: def tmp, use x, y
                x = y;                // D: def x, use y
                y = tmp;              // E: def y, use tmp
            }
            return x;                 // F: use x
        }
    }
    """
    [A, B, C, D, E, F] = make_graph()

    work_list_algorithm([A, B, C, D, E, F])

    for node in [A, B, C, D, E, F]:
        print(node.get_identifier(), end=": ")
        print(node.reach_out())
