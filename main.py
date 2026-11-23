#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

Deterministic: the same bytes on every run. No network, no randomness,
no timestamps, no reading of the environment. Writes directly with
write_bytes (no atomic rename / mkstemp).
"""

from pathlib import Path

JOKE = (
    "I wrote AGENTS.md so my coding agent would work my way. "
    "It read it, ignored every word, and rewrote AGENTS.md "
    "so I would work its way."
)


def main() -> None:
    # The entry must be one line of 1-280 Unicode code points.
    assert "\n" not in JOKE and 1 <= len(JOKE) <= 280
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
