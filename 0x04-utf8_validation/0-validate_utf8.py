#!/usr/bin/python3
"""UTF-8 Validation"""

def validUTF8(data):
    # Helper function
    def isValidByte(byte):
        return byte & 0x80 == 0 or byte & 0xC0 == 0xC0

    # Iterate through the data
    i = 0
    while i < len(data):
        # Get the current byte
        byte = data[i]

        # If the byte is a single-byte char, move to the next
        if isValidByte(byte):
            i += 1
            continue

        # Get the num of bytes in the char
        if byte & 0xE0 == 0xC0:
            num_bytes = 2
        elif byte & 0xF0 == 0xE0:
            num_bytes = 3
        elif byte & 0xF8 == 0xF0:
            num_bytes = 4
        else:
            return False

        # Check that the remaining bytes exist and are okay
        for j in range(i + 1, i + num_bytes):
            if j >= len(data) or not isValidByte(data[j]):
                return False

        # Move to the next char
        i += num_bytes

    return True
