# YouTube Description — Valid Parentheses

Learn how to solve **Valid Parentheses** (LeetCode #20) using a Stack — the
same trick your code editor uses to catch mismatched brackets as you type.
We build the intuition with hand-drawn stack animations, trace both a failing
and a passing case, then write the full solution in ~6 lines.

⏱️ Chapters
0:00  The hook — how editors catch bracket errors
0:15  The problem & the 3 rules
1:00  Key insight: last opened, first closed → Stack
1:45  Trace the tricky case: ([)]
4:30  Trace a valid case: {[]}
5:30  The three ways a string fails
6:15  The code, line by line
7:15  Time & space complexity
7:45  Summary

🧠 The idea in one line
Open bracket → push. Close bracket → check the top & pop if it matches.
At the end → the stack must be empty.

⚡ Complexity
Time:  O(n) — each character visited once
Space: O(n) — worst case all opens sit on the stack

💻 Code (Python)

```python
def is_valid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:                       # close bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:                                      # open bracket
            stack.append(char)

    return len(stack) == 0
```

🔗 Related videos
▶️ Implement Queue using Stacks: https://youtu.be/w28FYiaGE3Q

#DataStructures #Stack #Python #LeetCode #CodingInterview #ValidParentheses #DSA
