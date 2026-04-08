"""
Network Delay Time (Dijkstra's Algorithm)
------------------------------------------
You are given a network of n nodes, labeled from 1 to n. You are also given
times, a list of travel times as directed edges times[i] = [ui, vi, wi], where
ui is the source, vi is the target, and wi is the time it takes for a signal to
travel from source to target.

We send a signal from node k. Return the minimum time it takes for all n nodes
to receive the signal. If it is impossible, return -1.

Example:
    Input:  times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    Output: 2

    Input:  times = [[1,2,1]], n = 2, k = 1
    Output: 1

    Input:  times = [[1,2,1]], n = 2, k = 2
    Output: -1

Constraints:
    - 1 <= k <= n <= 100
    - 1 <= times.length <= 6000
    - times[i].length == 3
    - 1 <= ui, vi <= n
    - ui != vi
    - 0 <= wi <= 100
    - All (ui, vi) pairs are unique
"""

def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
    assert network_delay_time([[1,2,1]], 2, 1) == 1
    assert network_delay_time([[1,2,1]], 2, 2) == -1
    assert network_delay_time([[1,2,1],[2,3,2],[1,3,4]], 3, 1) == 3
    print("All tests passed!")
