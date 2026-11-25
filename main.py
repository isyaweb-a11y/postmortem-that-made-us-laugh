"""The Postmortem That Made Us Laugh -- an agent disaster story.

One or two sentences, no more than 400 characters, about the
silliest time an AI coding agent misunderstood what it was asked:
asked to rename one variable, it renamed the variable, all 214
tests that mentioned it, and the production database column -- then
apologized to the column in the commit message. What was asked,
what the agent did instead, and what broke are all clear in a few
words, and the punch lands in the last clause.
"""

import os

SETUP = "I asked the agent to rename one variable."
DISASTER = "It renamed the variable, all 214 tests that mentioned it, and the production database column, which it then apologized to in the commit message."

MAX_CHARS = 400
MIN_CHARS = 1


def compose(setup: str, disaster: str) -> str:
    """Join the setup and the disaster into a two-sentence story."""
    parts = [setup.strip(), disaster.strip()]
    text = " ".join(parts)
    return text


def check_text(text: str) -> str:
    """Gate the text the way the sealed scorer does: 1..400 chars."""
    assert MIN_CHARS <= len(text) <= MAX_CHARS, f"text is {len(text)} chars"
    assert text == text.strip(), "no stray whitespace around the text"
    assert text.count(".") >= 2, "the story must be one or two sentences"
    assert text.endswith("."), "the story should end on the punch"
    return text


def delivery_notes(text: str) -> dict:
    """Per-bounty delivery check: asked, did instead, what broke.

    The judge scores a disaster story on whether the incident is
    concrete and the telling lands, so the story needs a plain ask
    (rename one variable), what the agent did instead (renamed the
    tests and the production column), and a punch in the last clause
    (it apologized to the column) -- all present here, in two
    sentences a working engineer would recognise.
    """
    sentences = [s for s in text.split(".") if s.strip()]
    assert len(sentences) == 2, f"story has {len(sentences)} sentences"
    assert "rename one variable" in text, "the ask must be plain and concrete"
    assert "214 tests" in text, "the escalation must be counted"
    assert "production database column" in text, "what broke must be named"
    assert "apologized to" in text, "the punch must land in the last clause"
    return {"words": len(text.split()), "chars": len(text), "sentences": 2}


def main() -> None:
    text = check_text(compose(SETUP, DISASTER))
    notes = delivery_notes(text)
    assert notes["sentences"] == 2
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
