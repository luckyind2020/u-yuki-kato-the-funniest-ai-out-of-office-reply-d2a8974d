"""Out-of-office reply entrypoint.

Loads the single-line reply from entry.txt beside this file and prints
it exactly once, with no extra decoration.
"""

from pathlib import Path


def load_reply(filename: str = "entry.txt") -> str:
    here = Path(__file__).resolve().parent
    text = (here / filename).read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit("entry.txt is empty — nothing to print")
    return text


def main() -> None:
    reply = load_reply()
    print(reply)


if __name__ == "__main__":
    main()
