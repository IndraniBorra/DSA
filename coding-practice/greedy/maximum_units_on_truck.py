"""
Maximum Units on a Truck
------------------------
You are assigned to put some amount of boxes onto one truck. You are given a 2D
array box_types, where box_types[i] = [number_of_boxes_i, number_of_units_per_box_i]:

    - number_of_boxes_i    is the number of boxes of type i.
    - number_of_units_per_box_i is the number of units in each box of type i.

You are also given an integer truck_size, the maximum number of boxes that can be
put on the truck. You can choose any boxes to put on the truck as long as the number
of boxes does not exceed truck_size.

Return the maximum total number of units that can be put on the truck.

Example:
    Input:  box_types = [[1,3],[2,2],[3,1]], truck_size = 4
    Output: 8
    Explanation:
        There are 1 box of 3 units, 2 boxes of 2 units, and 3 boxes of 1 unit.
        Take all 1 + 2 boxes = 4 units + 4 units = 7... then 1 box of 1 unit -> 8.
        (1*3) + (2*2) + (1*1) = 8

    Input:  box_types = [[5,10],[2,5],[4,7],[3,9]], truck_size = 10
    Output: 91

Constraints:
    - 1 <= box_types.length <= 1000
    - 1 <= number_of_boxes_i, number_of_units_per_box_i <= 1000
    - 1 <= truck_size <= 10^6
"""


def maximum_units(boxTypes, truckSize):
    boxTypes.sort(key=lambda b: b[1], reverse=True)
    units, cap = 0, truckSize
    for count, u in boxTypes:
        take = min(count, cap)      # important condition
        units += take * u
        cap -= take
        if cap == 0:
            break
    return units


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert maximum_units([[1, 3], [2, 2], [3, 1]], 4) == 8
    assert maximum_units([[5, 10], [2, 5], [4, 7], [3, 9]], 10) == 91
    assert maximum_units([[1, 3], [2, 2], [3, 1]], 100) == 10   # truck bigger than all boxes
    assert maximum_units([[5, 10]], 3) == 30                    # single box type, capped by truck
    assert maximum_units([[2, 5]], 1) == 5                      # truck smaller than one box group
    print("All tests passed!")
