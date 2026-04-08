"""
Number of Connected Components in an Undirected Graph
-------------------------------------------------------
You have a graph of n nodes. You are given an integer n and an array edges
where edges[i] = [ai, bi] indicates there is an edge between ai and bi.

Return the number of connected components in the graph.

Example:
    Input:  n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2

    Input:  n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
    Output: 1

Constraints:
    - 1 <= n <= 2000
    - 1 <= edges.length <= 5000
    - edges[i].length == 2
    - 0 <= ai <= bi < n
    - ai != bi
    - There are no repeated edges
"""

def count_components(n: int, edges: list[list[int]]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert count_components(5, [[0,1],[1,2],[3,4]]) == 2
    assert count_components(5, [[0,1],[1,2],[2,3],[3,4]]) == 1
    assert count_components(4, []) == 4
    assert count_components(1, []) == 1
    print("All tests passed!")
