#!/usr/bin/python3
"""check if all boxes can be opened"""


def canUnlockAll(boxes):
    """check boxes to see if it contains keys to unlock
    else return false"""
    if not boxes or not boxes[0]:
        return False
    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        visited.add(current_box)

        for key in boxes[current_box]:
            if key not in visited and 0 <= key < n:
                stack.append(key)

    return len(visited) == n
