"""
Task Scheduler
---------------
You are given an array of CPU tasks, each labeled with a letter from A to Z,
and a number n. Each CPU interval can be idle or allow the completion of one task.
Tasks can be completed in any order, but there is a cooldown interval of n between
two same tasks (i.e., same tasks must be at least n intervals apart).

Return the minimum number of CPU intervals required to complete all tasks.

Example:
    Input:  tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation: A→B→idle→A→B→idle→A→B

    Input:  tasks = ["A","A","A","B","B","B"], n = 0
    Output: 6   (no cooldown needed)

    Input:  tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
    Output: 16

Constraints:
    - 1 <= tasks.length <= 10^4
    - tasks[i] is an uppercase English letter
    - 0 <= n <= 100
"""

def least_interval(tasks: list[str], n: int) -> int:
    pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert least_interval(["A","A","A","B","B","B"], 2) == 8
    assert least_interval(["A","A","A","B","B","B"], 0) == 6
    assert least_interval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2) == 16
    assert least_interval(["A"], 5) == 1
    print("All tests passed!")
