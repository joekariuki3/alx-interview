# UTF-8 Validation

Method that determines if a given data set represents a valid UTF-8 encoding.

### Problem

Implement `validUTF8(data: List[int]) -> bool` where each int is a byte (0–255). Validate per UTF‑8 leading byte patterns and continuation bytes.

### Usage

```bash
python3 0-main.py
```

### Notes

- Accepts ASCII, 2-, 3-, and 4-byte sequences with proper `10xxxxxx` continuations.
