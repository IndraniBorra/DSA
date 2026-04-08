"""
Find K Closest Elements
------------------------
Given a sorted integer array arr, two integers k and x, return the k closest
integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than b if:
  |a - x| < |b - x|, or
  |a - x| == |b - x| and a < b

Example:
    Input:  arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]

    Input:  arr = [1,2,3,4,5], k = 4, x = -1
    Output: [1,2,3,4]

Constraints:
    - 1 <= k <= arr.length
    - 1 <= arr.length <= 10^4
    - arr is sorted in ascending order
    - -10^4 <= arr[i], x <= 10^4
"""

def find_closest_elements(arr: list[int], k: int, x: int) -> list[int]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert find_closest_elements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
    assert find_closest_elements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
    assert find_closest_elements([1, 2, 3, 4, 5], 2, 3) == [2, 3]
    assert find_closest_elements([1, 3, 5, 7, 9], 3, 6) == [3, 5, 7]
    print("All tests passed!")
