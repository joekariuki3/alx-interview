# Minimum Operations

Fewest operations to get exactly `n` 'H' characters using Copy All and Paste.

### Problem

Implement `minOperations(n)` returning the minimal number of operations to reach `n` Hs starting from one `H`. If impossible or `n < 2`, return `0`.

### Usage

```bash
python3 0-main.py
```

### Notes

This approach grows by pasting when `n - current` isn’t divisible by current, otherwise copy+paste when it is.
