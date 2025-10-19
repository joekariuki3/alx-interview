# Developer overview

Quick tips to run and validate the subprojects locally.

## Python environment

- Requires Python 3.8+.
- Recommended tools: venv, ruff/flake8 for linting.

Create and activate a virtual environment (optional):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -V
```

## Node.js (Star Wars API)

- Requires Node.js 16+.
- Install dependency once in the folder:

```bash
cd 0x06-starwars_api
npm install request
```

Run the script:

```bash
node 0-starwars_characters.js 1
```

## Common tips

- Most Python folders include `0-main.py` to demo the solution.
- For stdin-based scripts (log parsing), pipe a generator or your own file.
- Prefer readability over premature optimization; document assumptions in each README.
