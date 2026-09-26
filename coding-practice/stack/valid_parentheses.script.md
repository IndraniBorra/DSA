# Valid Parentheses — Video Script

**Legend for cues:**
🎙️ = narration (voiceover)  📝 = draw on reMarkable  🖼️ = show slide / typeset screen

---

## Slide 1 — Hook (0:00–0:15) 🖼️

🎙️ "Every time you type code, your editor instantly knows if your brackets
are mismatched — a red squiggle appears the moment something's off. How does
it do that so fast? By the end of this video, you'll be able to write that
validation by yourself . Let's go."

---

## Slide 2 — Problem (0:15–1:00) 🖼️

🎙️ "Here's the challenge. We're given a string made only of parenthesis —
round, square, and curly — and we have to decide: is it valid?

Given string is valid when three rules hold:
one — every open bracket is closed by the *same* type;
two — brackets close in the *correct order*;
three — every close bracket has a matching open bracket.

So `()` is valid. `()[]{}` is valid. But `(]` is invalid — wrong type.
And `([)]` is invalid — wrong order. That last one is the tricky case,
so keep an eye on it."

---

## Slide 3 — Key Insight (1:00–1:45) 📝 reMarkable

📝 Write by hand, one line at a time as you speak:
   - "Last opened  →  First closed"
   - underline "Last In, First Out"
   - big arrow → draw the word **STACK**

🎙️ "Here's the one idea the whole solution rests on. Think about which
bracket must close first. It's always the *most recently opened* one.
The last thing you opened is the first thing you must close.

Last in, first out — that is exactly how a Stack behaves. So the moment
you see 'last opened, first closed,' your brain should basically shout: that its a Stack."

---

## Slide 4 — Walkthrough of `([)]` (1:45–4:30) 📝 reMarkable

📝 BEFORE recording, pre-draw: the string `( [ ) ]` across the top with a
   small pointer triangle under the first char, and an empty vertical
   stack box on the right. During recording you only animate below.

🎙️ "Let's trace the tricky one, `([)]`, step by step. Two rules for our fingers:
if it's an *open* bracket, push it onto the stack. If it's a *close* bracket,
check the top of the stack for its match."

📝 Move pointer to `(`. Draw `(` dropping into the box with a down-arrow.
🎙️ "First character, open round bracket. Push it. Stack now holds one item."

📝 Move pointer to `[`. Draw `[` on top of `(`.
🎙️ "Next, open square bracket. Push it too. Now the stack has `[` on top,
`(` underneath."

📝 Move pointer to `)`. Draw a thick circle around the TOP item `[`.
🎙️ "Now a *close* round bracket. It doesn't get pushed — instead we look at
the top of the stack. The top is `[`. But a `)` needs a `(` to match.
`[` is not `(`..."

📝 Draw a big ✗ next to the stack. Write "return False".
🎙️ "...mismatch. The brackets are interleaved in the wrong order, so the
string is invalid. We stop immediately and return False. That's the
wrong-order case caught in one comparison."

---

## Slide 5 — Walkthrough of `{[]}` (4:30–5:30) 📝 reMarkable

📝 Pre-draw `{ [ ] }` across the top, pointer under first char, empty box.

🎙️ "Now let's watch a *valid* one, `{[]}`, so we see success too."

📝 Pointer `{` → push `{`.  Pointer `[` → push `[` on top.
🎙️ "Open curly, push. Open square, push. Stack: `[` on top, `{` below."

📝 Pointer `]` → circle top `[`, it matches → draw pop arrow lifting `[` out.
🎙️ "Close square. Top of stack is `[` — that's the match! So we pop it off.
Stack now just has `{`."

📝 Pointer `}` → circle top `{`, matches → pop it. Box is now empty.
🎙️ "Close curly. Top is `{` — matches again, pop it. String's done, and
the stack is empty."

📝 Write "empty ✓  →  return True".
🎙️ "An empty stack at the end means every open bracket found its partner.
Valid — return True."

---

## Slide 6 — The Two Failure Modes (5:30–6:15) 📝 reMarkable

📝 Write two labeled boxes:
   1. "Wrong type / wrong order → top doesn't match"  (small sketch: `(` vs `]`)
   2. "Leftover opens → stack NOT empty at end"        (sketch: `(` alone)
   3. "Extra close / empty stack → nothing to match"   (sketch: `]` with empty box)

🎙️ "So there are really only three ways a string fails.
One: a close bracket whose top-of-stack doesn't match — wrong type or order.
Two: we reach the end but the stack still has leftover open brackets.
Three: a close bracket arrives when the stack is empty — there's nothing to
match it against. Handle those three, and you've handled everything."

---

## Slide 7 — The Code (6:15–7:15) 🖼️ show code

🎙️ "Here's the whole thing. We keep a stack, and a mapping from each close
bracket to its matching open bracket.

We loop through each character. If it's a close bracket — meaning it's a key
in our mapping — we check two things: is the stack empty, or does the top not
match? Either way, return False. Otherwise, pop the match off.

If it's an open bracket, we just push it.

At the very end, we return whether the stack is empty. Six lines of real logic —
that's it."

---

## Slide 8 — Complexity (7:15–7:45) 🖼️

🎙️ "Complexity is clean. We touch each character exactly once, so time is
O(n). In the worst case — all open brackets — the stack holds all of them,
so space is O(n) as well. Fast and simple."

---

## Slide 9 — Summary (7:45–8:00) 🖼️

🎙️ "Three things to remember:
open bracket — push.
close bracket — check the top, and pop if it matches.
At the end — the stack must be empty.

Get that pattern once, and you can write this from memory in any language.
Code's in the description. Thanks for watching!"
