## Lockboxes

Determine if all boxes can be opened given keys inside boxes.

### Problem

Function `canUnlockAll(boxes)` where `boxes` is a list of lists; box `0` is unlocked. Each list holds keys to other boxes by index. Return `True` if you can open all boxes, else `False`.

### Usage

```bash
python3 main_0.py
```

### Complexity

- Time: O(N + K) in practice (N boxes, K keys processed)
- Space: O(N) for visited/keys
