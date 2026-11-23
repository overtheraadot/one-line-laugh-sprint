"""One-Line Laugh Sprint entry (account A / overtheraa).

Writes a single original funny line about everyday life to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic, no network, no model calls, no file reads.
"""

import os

LINE = (
    "My router waits for my one important video call, then dies — "
    "I'm convinced it keeps a calendar and holds a grudge."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
