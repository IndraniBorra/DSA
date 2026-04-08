"""
Median of Two Sorted Arrays
-----------------------------
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log(m + n)).

Example:
    Input:  nums1 = [1,3], nums2 = [2]
    Output: 2.0

    Input:  nums1 = [1,2], nums2 = [3,4]
    Output: 2.5

Constraints:
    - nums1.length == m, nums2.length == n
    - 0 <= m, n <= 1000
    - 1 <= m + n <= 2000
    - -10^6 <= nums1[i], nums2[i] <= 10^6
"""

def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
    assert find_median_sorted_arrays([0, 0], [0, 0]) == 0.0
    assert find_median_sorted_arrays([], [1]) == 1.0
    assert find_median_sorted_arrays([2], []) == 2.0
    assert find_median_sorted_arrays([1, 3], [2, 4]) == 2.5
    print("All tests passed!")
