# Episode 1 — Implement Queue using Stacks (LeetCode 232)

Code: `implement_queue_using_stacks.py` (`MyQueueBruteForce` + `MyQueue`)

Target length: 10–14 min. Speak conversationally. `[SCREEN: ...]` = what the viewer sees.

---

## Teaching arc
Understand → Brute force → Analyze → Optimize → Explain *why* → Compare.

| Segment | Duration | Show |
|---|---|---|
| Hook | ~15s | Title slide |
| Problem & constraints | ~1 min | Slide: 4 ops + example |
| Brute force | ~2–3 min | draw.io + VS Code |
| Brute-force complexity | ~30s | Small table |
| Optimal | ~3–4 min | draw.io pour + VS Code |
| Why it works | ~1–2 min | draw.io arrows |
| Complexity comparison | ~1 min | Comparison table |
| Recap | ~30s | Takeaway slide |

---

## Complexity tables (put on screen)

Brute force (costly push):

| op | time |
|---|---|
| push | O(n) |
| pop | O(1) |
| peek | O(1) |
| space | O(n) |

Comparison:

| Approach | push | pop | peek | space |
|---|---|---|---|---|
| Brute force (costly push) | O(n) | O(1) | O(1) | O(n) |
| Optimal (lazy, 2 stacks) | O(1) | Amortized O(1) (worst O(n)) | Amortized O(1) | O(n) |

---

## Spoken script

**1. Hook (~15s)** — `[SCREEN: title slide "Queue using Stacks"]`
"A queue is first-in-first-out. A stack is last-in-first-out — the exact opposite. So how do you build a queue using only stacks? This is a classic interview question, and by the end you'll see one small trick that makes it click."

**2. Problem & constraints (~1 min)** — `[SCREEN: slide with the 4 operations + one example]`
"We need four operations: push adds to the back, pop removes from the front, peek looks at the front, and empty tells us if it's empty. The catch: we can only use stack operations — push to the top, pop from the top, peek the top. Let's say we push 1 then 2. The front is 1, because it came first. So pop should give us 1, not 2. Edge case to remember: never pop from an empty queue."

**3. Brute force (~2–3 min)** — `[SCREEN: draw.io, then VS Code live coding]`
"Simplest idea: what if the front element is always sitting on top of the stack, ready to go? To do that, every time we push, we rearrange. Move everything from stack one into a helper stack two, push the new element onto the now-empty stack one, then pour stack two back on top."
`[SCREEN: draw the two stacks moving elements]`
"Now the oldest element is always on top, so pop and peek are trivial. Let's code it and run it." `[live code MyQueueBruteForce, run terminal → tests pass]`

**4. Brute-force complexity (~30s)** — `[SCREEN: small table]`
"But look at the cost. Every single push moves all n elements twice — that's O(n) per push. Pop and peek are O(1). If we're pushing a lot, this is slow. Can we do better?"

**5. Optimal (~3–4 min)** — `[SCREEN: draw.io, then VS Code]`
"Here's the key realization: we were doing the expensive reshuffle on every push — even when nobody asked to pop. What if we're lazy and only rearrange when we actually need the front? We keep two stacks with jobs: an in-stack for pushing, an out-stack for popping. Push just drops onto the in-stack — done, O(1). When someone wants the front and the out-stack is empty, THEN we pour the in-stack into the out-stack. That pour reverses the order, so the oldest element lands on top of the out-stack." `[SCREEN: animate the pour, oldest ends on top]`
"Let's code exactly this." `[live code the existing MyQueue, run → tests pass]`

**6. Why it works / the condition (~1–2 min)** — `[SCREEN: draw.io arrows]`
"Two things make this correct and fast. First, why it's correct: pouring one stack into another reverses the order. A stack reverses once, a second stack reverses again — and two reversals give us back first-in-first-out. That's the whole trick. Second, why it's fast: notice we only pour when the out-stack is empty. That's the important condition — if you pour too early or on every push, you're back to the slow version. Because each element gets moved at most twice in its whole life — once in, once across — the total work stays O(n) over all operations. We call that amortized O(1): a single pop might occasionally be O(n), but averaged out, every operation is constant time."

**7. Complexity comparison (~1 min)** — `[SCREEN: comparison table above]`
"Side by side: brute force pays O(n) on every push. The optimal version pushes in O(1) and pops in amortized O(1). Same O(n) space. Same result, far less repeated work."

**8. Recap (~30s)** — `[SCREEN: one-line takeaway slide]`
"Two takeaways you can reuse on other problems: use a second stack to reverse order, and defer expensive work until it's actually needed. That lazy, amortized mindset shows up everywhere. If this helped, try coding it yourself without looking — that's where it sticks."

---

## Recording setup (laptop only)
- Screen record + voiceover: OBS / QuickTime.
- Slides & animation: **Canva Pro**. Stack diagrams: **draw.io**.
- VS Code font 16–18pt; run tests in terminal on camera.
- Edit in CapCut / DaVinci Resolve.

## Animation storyboard
See Part E in the plan — to be built next session (draw.io frames + Canva animation for the stack-pour sequence).
