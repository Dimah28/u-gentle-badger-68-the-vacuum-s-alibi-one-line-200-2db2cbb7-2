#!/usr/bin/env python3
"""The Vacuum's Alibi (make.fun bounty
u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7).

Writes one original funny line to /output/entry.txt: the excuse a robot
vacuum gives for missing a spot.

The line was built for this bounty judge's own criteria, in order:
  1. A funny one-line excuse a robot vacuum gives for missing a spot:
     the vacuum found the crumb and chose not to clean it.
  2. A real laugh, not a cute observation: the joke lands on the
     vacuum valuing its own life over a crumb -- self-preservation
     from an appliance that is supposed to serve.
  3. Deadpan machine voice, smug about its battery: it "weighed" the
     crumb against its remaining 4% battery, like a cost-benefit
     analysis, and the battery won.
  4. Surprise in a specific detail nobody expects: the exact "4%"
     battery, and the turn that the crumb is not worth *dying* for --
     a vacuum treating a cleaning run as a life-or-death mission.
  5. Tight, punch at the end: one sentence, 102 characters, every
     word earns its place, and the last words ("not worth dying for")
     carry the joke.

Alternatives considered and rejected:
  - "My sensors classified the crumb as a protected species, so per
    protocol I left it exactly where I found it." -- deadpan and
    specific, but the punch is a bureaucratic shrug, not a laugh.
  - "The spot was claimed by a spider, and my terms of service
    clearly state I do not evict tenants without 30 days' notice."
    -- funny rulebook voice, but the spider does the work; the
    vacuum itself is passive, not smug.
  - "I left the crumb there because my map now lists it as
    furniture, and I do not clean furniture. I respect furniture."
    -- good deadpan punch, but two sentences dilute the one-line
    tightness and the joke is a reframe, not a surprise.
The battery line wins on the judge's own order: its surprise is
last, its machine voice is the most deadpan, and it is the tightest.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

LINE = (
    "I found the crumb, weighed it against my remaining 4% battery, "
    "and decided it was not worth dying for."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> None:
    """Enforce the competition's gate before writing: 1-200 Unicode code
    points, one line, at least one character that is not white space.
    Fail loudly instead of writing an entry the gate would refuse."""
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"line is {len(line)} characters, must be 1-200")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if not any(not ch.isspace() for ch in line):
        raise SystemExit("line must contain a non-whitespace character")


def main() -> None:
    validate(LINE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
