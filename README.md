# ALX Interview Practice Suite

Collection of algorithmic and systems interview challenges with clean, runnable solutions in Python and Node.js, test drivers, and brief write-ups.

## About

This repository groups several standalone problem sets (subprojects). Each subproject includes:

- A short problem statement and constraints
- A reference implementation
- A tiny runner or sample main for quick testing
- Complexity notes and tips

Use it to practice fundamentals (arrays, graphs, DP, parsing, backtracking) and to rehearse interview-style tasks.

## Project map

| Folder                    | Title              | Lang    | What you’ll practice                    |
| ------------------------- | ------------------ | ------- | --------------------------------------- |
| `0x00-pascal_triangle`    | Pascal’s Triangle  | Python  | 2D arrays, iteration, edge cases        |
| `0x01-lockboxes`          | Lockboxes          | Python  | Graph reachability, set/queue reasoning |
| `0x02-minimum_operations` | Minimum Operations | Python  | Greedy/factors reasoning, loops         |
| `0x03-log_parsing`        | Log Parsing        | Python  | Streaming stdin, regex, counters        |
| `0x04-utf8_validation`    | UTF-8 Validation   | Python  | Bit/byte rules, linear scans            |
| `0x05-nqueens`            | N Queens           | Python  | Backtracking, pruning                   |
| `0x06-starwars_api`       | Star Wars API      | Node.js | REST calls, async/Promise patterns      |
| `0x07-rotate_2d_matrix`   | Rotate 2D Matrix   | Python  | In-place transforms, matrix math        |
| `0x08-making_change`      | Making Change      | Python  | Greedy vs DP trade-offs                 |
| `0x09-island_perimeter`   | Island Perimeter   | Python  | Grid traversal, neighbors               |
| `0x0A-primegame`          | Prime Game         | Python  | Simulation, primes, game turns          |

> [!TIP]
> Each folder has its own README with quick usage and complexity notes.

## Quick start

Prerequisites:

- Python 3.8+
- Node.js 16+ for the Star Wars API script

Clone and try a subproject:

```bash
git clone https://github.com/joekariuki3/alx-interview.git
cd alx-interview

# Example: run Pascal’s Triangle sample
python3 0x00-pascal_triangle/0-main.py
```

For the Star Wars API example, install its dependency once:

```bash
cd 0x06-starwars_api
npm init -y >/dev/null 2>&1
npm install request
node 0-starwars_characters.js 3
```

## How this repo is structured

- Each subproject is self-contained with minimal code to run directly.
- A `README.md` in each folder describes usage and expected behavior.
- Python solutions target clarity first, then efficiency where appropriate.

> [!NOTE]
> See `docs/overview.md` for environment tips and handy CLI snippets.

## Running the samples

Most Python folders include a small `0-main.py` to exercise the implementation. Run them directly with Python 3. For scripts that read from stdin (e.g., log parsing), use a generator or pipe your own logs. Node.js code is in `0x06-starwars_api`.

## Testing and style

- Keep solutions simple and readable; trade micro-optimizations for clarity unless otherwise noted.
- Use `flake8` or `ruff` if you prefer linting locally.
