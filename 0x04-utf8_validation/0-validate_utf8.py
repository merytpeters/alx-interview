#!/usr/bin/env python3
"""Valid UTF-8 Encoding"""


def validUTF8(data):
    """Checks that the data represents a valid UTF-8 encoding"""
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        byte = byte & 0xFF

        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
            else:
                if not (byte & mask1 and not (byte & mask2)):
                    return True
                num_bytes -= 1

    return num_bytes == 0
