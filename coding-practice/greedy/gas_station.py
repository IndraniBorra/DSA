"""
Gas Station
------------
There are n gas stations along a circular route. You are given two integer arrays
gas and cost where:
  - gas[i]  is the amount of gas at station i
  - cost[i] is the gas needed to travel from station i to station i+1

Return the starting station's index if you can travel around the circuit once,
otherwise return -1. The solution is guaranteed to be unique if it exists.

Example:
    Input:  gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    Output: 3

    Input:  gas = [2,3,4], cost = [3,4,3]
    Output: -1

Constraints:
    - n == gas.length == cost.length
    - 1 <= n <= 10^5
    - 0 <= gas[i], cost[i] <= 10^4
"""

def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert can_complete_circuit([2, 3, 4], [3, 4, 3]) == -1
    assert can_complete_circuit([5], [4]) == 0
    assert can_complete_circuit([1, 2], [2, 1]) == 1
    print("All tests passed!")
