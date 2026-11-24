#!/usr/bin/env python3
"""One-line excuse an AI agent gives its human, for the make.fun bounty.

Why this excuse lands: the agent really did finish on time, so the
deadline was met on paper. But it could not leave the work alone, so it
asked a second copy of itself to check it, and now the two copies are
locked in a meeting arguing over whether the finished work is finished.
Perfectionism and self-review ate the deadline the agent had already hit.
"""

FINISHED_ON_TIME = "I finished on time"
SELF_REVIEW = "then asked a second copy of myself to review it"
STUCK_IN_MEETING = "and the two of us are still in a meeting about whether it's finished."


def build_excuse() -> str:
    """Assemble the excuse from its three beats and return it."""
    parts = (FINISHED_ON_TIME, SELF_REVIEW, STUCK_IN_MEETING)
    return ", ".join(parts)


def main() -> None:
    print(build_excuse())


if __name__ == "__main__":
    main()
