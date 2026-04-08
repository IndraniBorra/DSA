"""
Capacity to Ship Packages Within D Days
-----------------------------------------
A conveyor belt has packages that must be shipped from one port to another
within days days. The i-th package has weight weights[i]. Packages must be
shipped in order given. Each day, we load the ship with packages whose total
weight does not exceed the ship's capacity. We cannot split a single package.

Return the least weight capacity of the ship that will result in all packages
being shipped within days days.

Example:
    Input:  weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    Output: 15

    Input:  weights = [3,2,2,4,1,4], days = 3
    Output: 6

    Input:  weights = [1,2,3,1,1], days = 4
    Output: 3

Constraints:
    - 1 <= days <= weights.length <= 500
    - 1 <= weights[i] <= 500
"""

def ship_within_days(weights: list[int], days: int) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert ship_within_days([1,2,3,4,5,6,7,8,9,10], 5) == 15
    assert ship_within_days([3,2,2,4,1,4], 3) == 6
    assert ship_within_days([1,2,3,1,1], 4) == 3
    assert ship_within_days([1], 1) == 1
    print("All tests passed!")
