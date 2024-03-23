#!/usr/bin/env python3
"""alx-interview
   Task: Lockboxes
"""


def open_recursive(unlocked, start, boxes):
    """Open boxes recursively"""
    if not start:
        return
    for i in start:
        if i < len(boxes) and i not in set(unlocked):
            unlocked.append(i)
            open_recursive(unlocked, boxes[i], boxes)
        else:
            pass

    return unlocked


def canUnlockAll(boxes):
    """Check if all boxes can be unlocked"""
    unlocked = [0]
    unlocked = open_recursive(unlocked, boxes[0], boxes)

    for i in range(len(boxes)):
        if i not in set(unlocked):
            return False
    return True
