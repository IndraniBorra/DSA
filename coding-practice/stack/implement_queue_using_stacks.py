"""
Implement Queue using Stacks
----------------------------
Implement a first in first out (FIFO) queue using only two stacks. The
implemented queue should support all the functions of a normal queue
(push, peek, pop, and empty).

Implement the MyQueue class:
  - push(x)  : Pushes element x to the back of the queue.
  - pop()    : Removes the element from the front of the queue and returns it.
  - peek()   : Returns the element at the front of the queue.
  - empty()  : Returns True if the queue is empty, False otherwise.

You must use only standard stack operations, i.e. push to top, peek/pop from
top, size, and is-empty are all valid.

Example:
    Input:  ["MyQueue","push","push","peek","pop","empty"]
            [[],[1],[2],[],[],[]]
    Output: [null, null, null, 1, 1, False]

Constraints:
    - 1 <= x <= 9
    - At most 100 calls will be made to push, pop, peek, and empty.
    - All the calls to pop and peek are valid.
"""

class MyQueueBruteForce:
    """
    Brute force — "costly push": keep the front element always on top of s1.
    Every push reshuffles the whole queue, so push is O(n) while pop/peek are O(1).
    """

    def __init__(self):
        self.s1 = []  # front element is always on top
        self.s2 = []  # helper

    def push(self, x: int) -> None:
        # Move everything to s2, put x at the bottom of s1, then pour s2 back.
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1


class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


# ── Tests ──────────────────────────────────────────────────────────────────────
def _run_tests(QueueClass) -> None:
    q = QueueClass()
    assert q.empty() == True
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() == False
    q.push(3)
    assert q.peek() == 2
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.empty() == True


if __name__ == "__main__":
    _run_tests(MyQueueBruteForce)
    _run_tests(MyQueue)
    print("All tests passed!")
