#!/usr/bin/python3

def canUnlockAll(boxes):
    """Unlock boxes"""
    if not boxes:
        return False
    n = len(boxes)
    # To track which boxes are unlocked
    unlocked = [False] * n
    # box 0 is always unlocked
    unlocked[0] = True
    # Start with keys in first box
    keys = boxes[0]

    for key in keys:
        # check if key is valid and box is locked
        if key < n and not unlocked[key]:
            unlocked[key] = True
            # Add keys from the newly unlocked box
            keys.extend(boxes[key])

    return all(unlocked)
