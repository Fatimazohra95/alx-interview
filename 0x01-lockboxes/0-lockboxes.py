#!/usr/bin/python3
'''LockBoxes Challenge'''

def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened or not.

    Args:
        boxes (list): A list of lists representing the lockboxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    '''
    if not boxes:
        return False

    num_boxes = len(boxes)
    keys = set()
    opened_boxes = set()
    stack = [0]

    while stack:
        box = stack.pop()
        if box not in opened_boxes:
            opened_boxes.add(box)
            keys.update(boxes[box])
            stack.extend(key for key in boxes[box] if 0 <= key < num_boxes)

    return len(opened_boxes) == num_boxes
