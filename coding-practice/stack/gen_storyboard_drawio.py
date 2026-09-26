"""
Generate a multi-page draw.io (.drawio) storyboard for the
"Implement Queue using Stacks" video animation.

Run:  python3 gen_storyboard_drawio.py
Output: implement_queue_using_stacks.storyboard.drawio
Open in draw.io (app.diagrams.net) via File > Open. Each page = one frame.
"""

import html

OUT = "implement_queue_using_stacks.storyboard.drawio"

# ── low-level cell builders ─────────────────────────────────────────────────────
_id = [10]


def nid():
    _id[0] += 1
    return f"c{_id[0]}"


def box(value, x, y, w=70, h=44, fill="#dae8fc", stroke="#6c8ebf", fontsize=16):
    return (
        f'<mxCell id="{nid()}" value="{html.escape(str(value))}" '
        f'style="rounded=0;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};'
        f'fontSize={fontsize};fontStyle=1;" vertex="1" parent="1">'
        f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>'
    )


def text(value, x, y, w=260, h=30, fontsize=16, bold=False, color="#000000", align="left"):
    style_bold = 1 if bold else 0
    return (
        f'<mxCell id="{nid()}" value="{html.escape(str(value))}" '
        f'style="text;html=1;align={align};verticalAlign=middle;fontSize={fontsize};'
        f'fontStyle={style_bold};fontColor={color};" vertex="1" parent="1">'
        f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>'
    )


def arrow(x1, y1, x2, y2, color="#b85450", label=""):
    return (
        f'<mxCell id="{nid()}" value="{html.escape(label)}" '
        f'style="endArrow=classic;html=1;strokeColor={color};strokeWidth=2;fontSize=14;fontStyle=1;" '
        f'edge="1" parent="1">'
        f'<mxGeometry relative="1" as="geometry">'
        f'<mxPoint x="{x1}" y="{y1}" as="sourcePoint"/>'
        f'<mxPoint x="{x2}" y="{y2}" as="targetPoint"/></mxGeometry></mxCell>'
    )


def stack(label, x, elements, base_y=600, fill="#dae8fc", stroke="#6c8ebf"):
    """Draw a stack column bottom-up. elements[0] = bottom, elements[-1] = top."""
    cells = []
    bw, bh = 90, 44
    # base line label
    cells.append(text(label, x, base_y + 12, w=bw, h=24, fontsize=15, bold=True))
    # base plate
    cells.append(
        f'<mxCell id="{nid()}" value="" style="line;strokeColor=#666666;strokeWidth=3;html=1;" '
        f'vertex="1" parent="1"><mxGeometry x="{x-5}" y="{base_y}" width="{bw+10}" height="6" as="geometry"/></mxCell>'
    )
    for i, e in enumerate(elements):
        ey = base_y - (i + 1) * (bh + 4)
        cells.append(box(e, x, ey, w=bw, h=bh, fill=fill, stroke=stroke))
    if elements:
        top_y = base_y - len(elements) * (bh + 4)
        cells.append(text("← top", x + bw + 8, top_y, w=70, h=bh, fontsize=13))
    return "\n".join(cells)


def page(name, body):
    return (
        f'<diagram name="{html.escape(name)}" id="{nid()}">'
        f'<mxGraphModel dx="800" dy="600" grid="1" gridSize="10" guides="1" '
        f'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageWidth="1280" '
        f'pageHeight="720" math="0" shade="1">'
        f'<root><mxCell id="0"/><mxCell id="1" parent="0"/>'
        f'{body}'
        f'</root></mxGraphModel></diagram>'
    )


# ── frame content ───────────────────────────────────────────────────────────────
GREEN = ("#d5e8d4", "#82b366")
BLUE = ("#dae8fc", "#6c8ebf")
YELLOW = ("#fff2cc", "#d6b656")

INX, OUTX = 460, 820  # centered pair on a 1280-wide canvas


def frame(title, subtitle, in_els, out_els, extras=""):
    body = [
        text(title, 40, 60, w=1200, h=44, fontsize=30, bold=True, align="center"),
        text(subtitle, 40, 110, w=1200, h=32, fontsize=18, color="#666666", align="center"),
        stack("in_stack", INX, in_els, fill=BLUE[0], stroke=BLUE[1]),
        stack("out_stack", OUTX, out_els, fill=GREEN[0], stroke=GREEN[1]),
        extras,
    ]
    return "\n".join(b for b in body if b)


frames = []

# Title
frames.append(("00 — Title", "\n".join([
    text("Implement Queue using Stacks", 40, 300, w=1200, h=60, fontsize=44, bold=True, align="center"),
    text("Optimal: two stacks, lazy transfer  ·  amortized O(1)", 40, 380, w=1200, h=36, fontsize=22, color="#666666", align="center"),
])))

# Optimal sequence
frames.append(("01 — Empty", frame(
    "Start: two empty stacks", "in_stack receives pushes · out_stack serves the front", [], [])))

frames.append(("02 — push(1)", frame(
    "push(1)", "Just drop onto in_stack. O(1).", [1], [],
    arrow(INX + 160, 430, INX + 60, 545, color="#b85450", label="push"))))

frames.append(("03 — push(2)", frame(
    "push(2)", "Still just in_stack. O(1).", [1, 2], [])))

frames.append(("04 — push(3)", frame(
    "push(3)", "in_stack = [1,2,3], top = 3. No reshuffle yet!", [1, 2, 3], [])))

frames.append(("05 — pop() needs front", frame(
    "pop() called — out_stack is empty", "Condition met → NOW we pour in_stack into out_stack.", [1, 2, 3], [],
    arrow(INX + 100, 490, OUTX - 10, 490, color="#d79b00", label="pour (only when out_stack empty)"))))

frames.append(("06 — after pour", frame(
    "Poured! Order reversed.", "in_stack emptied. out_stack top = 1 (the oldest = the front).", [], [3, 2, 1])))

frames.append(("07 — pop() returns 1", frame(
    "pop() → 1", "Pop top of out_stack. Correct FIFO front returned.", [], [3, 2],
    arrow(OUTX + 160, 380, OUTX + 60, 500, color="#b85450", label="pop → 1"))))

frames.append(("08 — pop() returns 2", frame(
    "pop() → 2", "out_stack not empty → no pour needed. O(1).", [], [3])))

# Why-it-works recap
frames.append(("09 — Why it works", "\n".join([
    text("Why it works", 40, 90, w=1200, h=50, fontsize=36, bold=True, align="center"),
    text("1) A pour REVERSES order. Stack reverses once, a second stack reverses", 120, 250, w=1040, h=36, fontsize=24),
    text("   again  →  two reversals = FIFO.", 120, 300, w=1040, h=36, fontsize=24),
    text("2) Pour ONLY when out_stack is empty (lazy). Pour early → slow O(n).", 120, 380, w=1040, h=36, fontsize=24),
    text("3) Each element moves at most twice (in, then across) → amortized O(1).", 120, 460, w=1040, h=36, fontsize=24),
])))

# Complexity comparison
frames.append(("10 — Complexity", "\n".join([
    text("Complexity", 40, 90, w=1200, h=50, fontsize=36, bold=True, align="center"),
    text("Brute force (costly push)", 120, 220, w=600, h=36, fontsize=24, bold=True),
    text("push O(n)  ·  pop O(1)  ·  peek O(1)  ·  space O(n)", 120, 265, w=900, h=36, fontsize=22),
    text("Optimal (lazy, 2 stacks)", 120, 350, w=600, h=36, fontsize=24, bold=True),
    text("push O(1)  ·  pop amortized O(1)  ·  peek amortized O(1)  ·  space O(n)", 120, 395, w=1040, h=36, fontsize=22),
    text("Takeaway: reverse with a 2nd stack + defer work until needed.", 40, 540, w=1200, h=40, fontsize=26, bold=True, color="#2d6a2d", align="center"),
])))

# ── brute-force mini sequence (optional B-roll) ─────────────────────────────────
def bf_frame(title, subtitle, s1, s2, extras=""):
    body = [
        text(title, 40, 60, w=1200, h=44, fontsize=30, bold=True, align="center"),
        text(subtitle, 40, 110, w=1200, h=32, fontsize=18, color="#666666", align="center"),
        stack("s1 (front on top)", INX, s1, fill=YELLOW[0], stroke=YELLOW[1]),
        stack("s2 (helper)", OUTX, s2, fill=BLUE[0], stroke=BLUE[1]),
        extras,
    ]
    return "\n".join(b for b in body if b)


frames.append(("B1 — Brute: have [1]", bf_frame(
    "Brute force — front always on top", "s1 = [1]. Now push(2)...", [1], [])))
frames.append(("B2 — Brute: pour to s2", bf_frame(
    "push(2): move s1 → s2", "Empty s1 into helper s2 first.", [], [1],
    arrow(INX + 100, 490, OUTX - 10, 490, color="#d79b00", label="move"))))
frames.append(("B3 — Brute: put new", bf_frame(
    "push(2): drop 2 on empty s1", "New element goes to the bottom.", [2], [1])))
frames.append(("B4 — Brute: pour back", bf_frame(
    "push(2): pour s2 back", "s1 = [2,1], front (1) on top. Every push does this → O(n).", [2, 1], [],
    arrow(OUTX - 10, 490, INX + 100, 490, color="#d79b00", label="move back"))))

# Brute-force complexity + redirect to the optimal solution
frames.append(("B5 — Brute complexity", "\n".join([
    text("Brute force — the cost", 40, 90, w=1200, h=50, fontsize=36, bold=True, align="center"),
    text("push  →  O(n)   (every insert reshuffles the whole stack)", 120, 240, w=1040, h=40, fontsize=26),
    text("pop   →  O(1)          peek  →  O(1)          space  →  O(n)", 120, 300, w=1040, h=40, fontsize=26),
    text("The push is the pain point. Can we do better?", 40, 420, w=1200, h=40, fontsize=26, bold=True, color="#b85450", align="center"),
    text("→  Let's see the optimal solution", 40, 500, w=1200, h=48, fontsize=30, bold=True, color="#2d6a2d", align="center"),
])))


# ── assemble ────────────────────────────────────────────────────────────────────
pages = "\n".join(page(name, body) for name, body in frames)
doc = f'<mxfile host="app.diagrams.net">\n{pages}\n</mxfile>\n'

with open(OUT, "w") as f:
    f.write(doc)

print(f"Wrote {OUT} with {len(frames)} frames.")
