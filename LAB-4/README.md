# Changes Made

## Task 1 – Coordinate Handling
- Made coordinate handling consistent across the game.
- User input is converted from 1-based coordinates to 0-based `(row, column)` tuples.
- AI now returns coordinates as `(row, column)` tuples.
- Added validation for invalid and out-of-range coordinates.
- Prevented repeated player shots.

## Task 2 – Fleet and Win Logic
- Added multiple ships:
  - Carrier
  - Battleship
  - Cruiser
  - Submarine
  - Destroyer
- Added individual ship hit tracking.
- Added ship sinking detection.
- Prevented ships from overlapping.
- Added complete fleet-sunk detection.
- Added player win and loss conditions.
- Added repeated-shot detection.
- Added remaining enemy ship-cell tracking.

## Task 3 – AI Improvements
- Added tracking of AI coordinates already tried.
- Prevented the AI from intentionally firing at the same coordinate twice.
- Added adjacent-cell targeting after an AI hit.
- Added target queue handling.
- Cleared the target queue when a ship is sunk.
- Added fallback to random untried coordinates.
- Added handling for when no valid AI shots remain.

## Task 4 – Shot Feedback
- Separated AI coordinate selection from actual shot execution.
- Added clear `HIT`, `MISS`, and `SUNK` feedback.
- Ensured each actual shot produces feedback only once.
- Prevented AI candidate selection from producing false shot results.
- Added separate feedback for player and AI shots.
- Added messages when a ship is sunk.
- Added messages when the complete fleet is destroyed.

## Files Changed

- `board.py`
- `ai.py`
- `game.py`

Repository link - https://github.com/shrutiburukule17/19-battleship
