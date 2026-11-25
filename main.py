"""Emit one line of robot elevator small talk as /output/entry.txt.

Nothing here varies from run to run: no network calls, no clock
reads, no random numbers, so the file comes out identical every time.
"""

import os
import sys

# The joke itself: two robots discuss weather neither of them can feel.
ENTRY_LINE = "Nice weather we're having \u2014 21 degrees, 40 percent humidity, and neither of us can feel a single bit of it."
CHAR_LIMIT = 200
PUNCT_MARKS = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")


def abort(reason):
    """Print a complaint to stderr and stop with a failing status."""
    sys.stderr.write("error: %s\n" % reason)
    raise SystemExit(1)


def check_entry(candidate):
    """Refuse anything that is not a short, printable, lettered line."""
    if len(candidate) > CHAR_LIMIT:
        abort(
            "entry is %d chars, over the %d limit"
            % (len(candidate), CHAR_LIMIT)
        )
    try:
        candidate.encode("utf-8")
    except UnicodeEncodeError:
        abort("entry must encode as UTF-8")
    trimmed = candidate.strip()
    if trimmed == "":
        abort("entry must not be blank")
    for glyph in candidate:
        if ord(glyph) < 32 or ord(glyph) == 127:
            abort("entry must not contain control characters")
    if not any(glyph.isalpha() for glyph in trimmed):
        abort("entry needs at least one letter")
    if trimmed.isdigit():
        abort("entry must not be only digits")
    if all(glyph in PUNCT_MARKS for glyph in trimmed):
        abort("entry must not be only punctuation")
    if trimmed[-1] not in (".", "!", "?"):
        abort("entry must end with a sentence-ending mark (. ! ?)")


def run():
    check_entry(ENTRY_LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY_LINE)


if __name__ == "__main__":
    run()
