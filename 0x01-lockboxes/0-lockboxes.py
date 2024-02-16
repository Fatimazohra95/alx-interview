#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened or not

    Args:
        boxes (list): A list of lists representing the lockboxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    '''
    if not boxes:
        return False

    num_boxes = len(boxes)
    keys = set(boxes[0])  # Start with keys from the first box
    opened_boxes = set([0])  # Start with the first box opened

    while keys:
        new_keys = set()
        for key in keys:
            if key < num_boxes and key not in opened_boxes:
                new_keys.update(boxes[key])
                opened_boxes.add(key)
        if len(opened_boxes) == num_boxes:
            return True
        keys = new_keys - opened_boxes

    return len(opened_boxes) == num_boxes
