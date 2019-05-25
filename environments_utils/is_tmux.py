import os

def is_tmux()->bool:
    """Return a boolean representing if script is running within a TMUX-like terminal."""
    return "TMUX" in os.environ