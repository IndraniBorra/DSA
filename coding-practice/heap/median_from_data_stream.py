"""
Median From Data Stream
------------------------
Design a data structure that supports the following operations:
  - addNum(num): Add an integer num from the data stream to the data structure.
  - findMedian(): Return the median of all elements so far.

If the size of the list is even, the median is the mean of the two middle values.

Example:
    MedianFinder mf = MedianFinder()
    mf.addNum(1)    → data = [1]
    mf.addNum(2)    → data = [1,2]
    mf.findMedian() → 1.5
    mf.addNum(3)    → data = [1,2,3]
    mf.findMedian() → 2.0

Constraints:
    - -10^5 <= num <= 10^5
    - There will be at least one element before calling findMedian
    - At most 5 * 10^4 calls will be made to addNum and findMedian
"""

class MedianFinder:

    def __init__(self):
        pass

    def add_num(self, num: int) -> None:
        pass

    def find_median(self) -> float:
        pass


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    assert mf.find_median() == 1.5
    mf.add_num(3)
    assert mf.find_median() == 2.0
    mf.add_num(4)
    assert mf.find_median() == 2.5
    mf.add_num(5)
    assert mf.find_median() == 3.0
    print("All tests passed!")
