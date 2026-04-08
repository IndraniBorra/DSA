"""
Daily Temperatures
-------------------
Given an array of integers temperatures representing the daily temperatures,
return an array answer such that answer[i] is the number of days you have to
wait after the i-th day to get a warmer temperature. If there is no future
day for which this is possible, keep answer[i] == 0.

Example:
    Input:  temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]

    Input:  temperatures = [30,40,50,60]
    Output: [1,1,1,0]

    Input:  temperatures = [30,60,90]
    Output: [1,1,0]

Constraints:
    - 1 <= temperatures.length <= 10^5
    - 30 <= temperatures[i] <= 100
"""

def daily_temperatures(temperatures: list[int]) -> list[int]:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0]
    assert daily_temperatures([90, 80, 70]) == [0, 0, 0]
    print("All tests passed!")
