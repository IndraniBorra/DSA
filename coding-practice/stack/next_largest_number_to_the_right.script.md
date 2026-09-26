# Next Largest Number to the Right — Video Script

**Legend for cues:**
🎙️ = narration (voiceover)  📝 = draw on reMarkable  🖼️ = show slide / typeset screen

Example used throughout: **nums = [5, 2, 4, 6, 1] → res = [6, 4, 6, -1, -1]**

---

## Slide 1 — Hook (0:00–0:15) 🖼️

🎙️ "You're looking at a row of stock prices. For each day, you want the next
day the price jumps higher. Check every day against every future day and it's
slow. But there's a way to get every answer in a single pass — using a stack.
Let's build it."

---

## Slide 2 — Problem (0:15–1:00) 🖼️

🎙️ "Here's the problem. We're given an array of numbers. For each number, we
want the first number to its right that is strictly larger. If nothing to the
right is larger, we write minus one.

Take `[5, 2, 4, 6, 1]`. For the 5, scan right — 2, 4, both smaller, then 6:
that's our answer. For the 2, the next larger is 4. For the 4, it's 6. For the
6, nothing to the right is bigger, so minus one. And the last element, 1, has
nothing to its right at all — minus one. Result: `[6, 4, 6, -1, -1]`."

---

## Slide 3 — Brute Force & the Shift (1:00–2:15) 🖼️ / 📝

🖼️ Show the O(n²) idea briefly.
🎙️ "The obvious solution: for every number, walk right until you find a bigger
one. That works, but it's O(n squared) — for each of n numbers we might scan
the whole rest of the array. Can we do better?

Let's flip the question. Instead of asking 'what's the next larger number for
this value?', ask: 'for which earlier values could THIS value be the answer?'"

📝 (reMarkable) Draw the bars for [5, 2, 4, 6, 1]. Circle the 6 and draw arrows
back to the 5 and the 4.
🎙️ "Look at 6. It's the next larger number for both 5 and 4 sitting to its
left. So if we scan from the RIGHT, each value we pass could be the answer for
things further left. Call these values our 'candidates.'"

---

## Slide 4 — Which candidates survive? (2:15–4:00) 📝 reMarkable

📝 Pre-draw the array [5, 2, 4, 6, 1]. You'll build the candidate list on the
   right as you scan leftward.

🎙️ "Now the key question: which numbers are worth keeping as candidates?

Scan right to left. We meet 1 — keep it. We meet 6. Is 1 still useful? No —
6 is both larger AND further left, so 6 will always beat 1 for anyone on the
left. Drop the 1. Whenever a new number appears, throw away every candidate
less than or equal to it."

📝 Show candidates shrinking: [1] → 6 arrives → drop 1 → [6].
🎙️ "That single rule keeps our candidate list in strictly DECREASING order —
biggest at the bottom, smallest on top. And 'add to top, remove from top' is
exactly a stack. A monotonic decreasing stack."

---

## Slide 5 — Full Walkthrough (4:00–6:15) 📝 reMarkable

📝 Pre-draw array [5, 2, 4, 6, 1] with a pointer, an empty vertical stack, and
   an empty res array of 5 slots. Animate right to left.

🎙️ "Let's run the whole thing. Stack starts empty. Rules at each step: pop
everything on top that's ≤ the current number; whatever's left on top is the
answer (or minus one if empty); then push the current number."

📝 i=4, value 1: stack empty → res[4] = -1 → push 1.  Stack: [1]
🎙️ "Rightmost is 1. Stack empty, so answer is minus one. Push 1."

📝 i=3, value 6: pop 1 (1≤6) → empty → res[3] = -1 → push 6.  Stack: [6]
🎙️ "Next is 6. Pop the 1 — it's smaller. Stack empty, answer minus one. Push 6."

📝 i=2, value 4: top 6 > 4 → res[2] = 6 → push 4.  Stack: [6, 4]
🎙️ "Now 4. Top of stack is 6, bigger than 4 — that's the answer, 6. Push 4."

📝 i=1, value 2: top 4 > 2 → res[1] = 4 → push 2.  Stack: [6, 4, 2]
🎙️ "Now 2. Top is 4, bigger — answer 4. Push 2. Notice the stack: 6, 4, 2 —
decreasing, top to bottom bottom to top."

📝 i=0, value 5: pop 2 (≤5), pop 4 (≤5), top 6 > 5 → res[0] = 6 → push 5.
   Stack: [6, 5]
🎙️ "Finally 5. Pop 2, pop 4 — both too small to ever beat 5. Now the top is 6,
which is bigger — answer 6. Push 5. Done."

📝 Reveal res = [6, 4, 6, -1, -1].
🎙️ "Result: 6, 4, 6, minus one, minus one. Exactly what we wanted."

---

## Slide 6 — The Code (6:15–7:15) 🖼️ show code

🎙️ "Here's the code. res holds our answers, stack holds the candidates. We
loop i from the last index down to zero. While the stack's top is ≤ the current
value, pop it. Then res[i] is the top of the stack if there is one, otherwise
minus one. Finally, push the current value as a new candidate. That's the whole
algorithm."

---

## Slide 7 — Complexity + Takeaway (7:15–8:00) 🖼️

🎙️ "Why is this fast? Each value is pushed once and popped at most once — so
even with the inner while-loop, the total work is O(n), one pass. Space is O(n)
for the stack.

The big idea: a MONOTONIC STACK. When a problem asks for the next greater — or
next smaller — element, keep a stack in sorted order and pop what can't win.
The same pattern solves Daily Temperatures, stock spans, and more. Code's in
the description. Thanks for watching!"
