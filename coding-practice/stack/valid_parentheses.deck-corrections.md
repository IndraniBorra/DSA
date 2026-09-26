# Valid Parentheses — Corrected Deck Content

Apply these to the source deck, then re-export the PDF.
✅ = correct as-is · 🔴 = must fix

---

## Slide 1 — Hook ("Your code editor does this 1000 times a second")

🔴 **Valid example is wrong.**

| Currently shows | Corrected |
|---|---|
| `"({[]))"  ->  Valid ✓` | `"({[]})"  ->  Valid ✓` |
| `"({))"    ->  Invalid ✗` | `"({))"    ->  Invalid ✗` (already correct) |

Why: `"({[]))"` fails — after `]` pops `[`, the next `)` meets `{` → mismatch.
The intended valid string is `"({[]})"` → `( { [ ] } )`, which fully matches.

🟡 Optional: the code snippet on the right shows `{f (arr[i] == "(")`.
If the broken code + red squiggle is intentional (showing what an editor
flags), leave it. Otherwise change `{f` → `if`.

---

## Slide 2 — Problem (LeetCode 20)

Use the exact LeetCode wording and clean input/output.

**Title:** LeetCode 20: Valid Parentheses
**Subtitle:** Every close bracket must match the most recent unmatched open

**Question (left box):**
> Given a string `s` containing just the characters
> `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`,
> determine if the input string is valid.
>
> An input string is valid if:
> 1. Open brackets are closed by the **same type** of bracket.
> 2. Open brackets are closed in the **correct order**.
> 3. Every close bracket has a **matching open** bracket of the same type.

**Input / Output Examples (right box) — REPLACE all four:**

🔴 The current examples have three wrong outputs. Corrected set:

| Input            | Output  | Why                          |
|------------------|---------|------------------------------|
| `s = "()"`       | `true`  | simple match                 |
| `s = "()[]{}"`   | `true`  | three independent pairs      |
| `s = "(]"`       | `false` | wrong **type** — `(` vs `]`  |
| `s = "([)]"`     | `false` | wrong **order** — interleaved|

(These are the canonical LeetCode examples plus the classic wrong-order case.)

Format each as:
  Input:  s = "()"
  Output: true

---

## Slide 3 — How Stack Solves It

🔴 **Two fixes.**

**1. Algorithm bullet (right side).**

| Currently shows | Corrected |
|---|---|
| `if char is { { [ → push` | `if char is ( { [ → push` |

(It listed two `{`. The three OPEN brackets are `(`, `{`, `[`.)

Full corrected algorithm block:
  • if char is ( { [        → push
  • else (a close bracket)  → if stack empty OR top ≠ matching open → return false
  • otherwise               → pop()
  • at the end              → return (stack is empty)

**2. Example trace (bottom).**

| Currently shows | Corrected |
|---|---|
| `( → { → [ → ] → ] → } → )` | `( → { → [ → ] → } → )` |

(Had an extra `]`. The string is `s = "({[]})"` = 6 characters, so the
trace is 6 tiles: `( { [ ] } )`.)

Header string `s = "({[]})"` ✅ correct — keep it.

---

## Slide 4 — Complexity + Takeaway

✅ Correct. No changes.
  Time O(n) · Space O(n) · Push/Pop O(1) · Takeaway text all accurate.

---

## Quick summary of every change

1. Slide 1: `"({[]))"` → `"({[]})"` (valid example)
2. Slide 1 (optional): `{f` → `if` in code snippet
3. Slide 2: replace all 4 input/output pairs (see table)
4. Slide 3: `{ { [` → `( { [` in algorithm
5. Slide 3: remove the extra `]` in the trace → `( { [ ] } )`
