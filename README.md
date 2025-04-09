# pgn-purifier

**pgn-purifier** is a simple Python tool that strips away all non-essential elements from PGN (Portable Game Notation) files — including annotations, comments, variations, and engine evaluations — leaving you with clean, readable move sequences.

## ✨ Features

- Removes:
  - Comments (`{ ... }`)
  - Engine annotations (`[%eval ...]`, `[%cal ...]`, etc.)
  - Variations (`( ... )`)
  - Move annotations (`!`, `?`, `!?`, `??`, etc.)
- Outputs a pure PGN with just the mainline moves
- Easy to use from the command line

## 📦 Installation

Just clone the repo and run the script:

```bash
python3 purify.py your_game.pgn
