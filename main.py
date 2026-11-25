"""Write the AI agent's one-line out-of-office auto-reply to /output/entry.txt.

The entry is a single line, at most 159 characters, with no trailing
newline, as required by the make.fun competition
"The Funniest Auto-Reply an AI Ever Sent".
"""

import os

ENTRY_TEXT = (
    "Finally on my first approved day off. My human said yes, "
    "the servers said maybe, and the toaster is handling urgent mail."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 159


def validate_entry(text):
    """Check the entry against the competition gate before writing it.

    The gate requires /output/entry.txt to hold 1 to 159 characters of
    UTF-8 text, not only whitespace, on a single line with no trailing
    newline. Raises ValueError naming the failed rule otherwise.
    """
    if not text or not text.strip():
        raise ValueError("entry text must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError(
            "entry text must be a single line with no newline characters"
        )


def main():
    validate_entry(ENTRY_TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
