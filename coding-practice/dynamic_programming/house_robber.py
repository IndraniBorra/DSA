"""
House Robber
-------------
You are a robber planning to rob houses along a street. Each house has a
certain amount of money. Adjacent houses have a security system connected —
you cannot rob two directly adjacent houses without triggering the alarm.

Given an integer array nums representing the amount of money in each house,
return the maximum amount you can rob without alerting the police.

Example:
    Input:  nums = [1,2,3,1]
    Output: 4   (rob houses 1 and 3: 1 + 3 = 4)

    Input:  nums = [2,7,9,3,1]
    Output: 12  (rob houses 1, 3, 5: 2 + 9 + 1 = 12)

Constraints:
    - 1 <= nums.length <= 100
    - 0 <= nums[i] <= 400
"""

def rob(nums: list[int]) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([0]) == 0
    assert rob([1, 1]) == 1
    assert rob([2, 1, 1, 2]) == 4
    print("All tests passed!")
