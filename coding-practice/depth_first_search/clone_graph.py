"""
Clone Graph
------------
Given a reference of a node in a connected undirected graph, return a deep
copy (clone) of the graph. Each node contains a value (int) and a list of its neighbors.

Example:
    Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]   (4-node cycle graph)
    Output: Deep copy of the same structure

    Input:  adjList = [[]]
    Output: [[]]

    Input:  adjList = []   (empty graph)
    Output: []

Constraints:
    - The number of nodes is in the range [0, 100]
    - 1 <= Node.val <= 100
    - Node.val is unique for each node
    - There are no repeated edges and no self-loops in the graph
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node) -> Node:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Build: 1 -- 2 -- 3 -- 4 -- 1
    n1 = Node(1); n2 = Node(2); n3 = Node(3); n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n3, n1]

    cloned = clone_graph(n1)
    assert cloned is not n1          # must be a new object
    assert cloned.val == 1
    assert len(cloned.neighbors) == 2
    assert cloned.neighbors[0] is not n2   # deep copy

    assert clone_graph(None) is None

    print("All tests passed!")
