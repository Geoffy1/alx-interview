#!/usr/bin/python3
"""UTF-8 Validation""

def validUTF8(data):
    expected_continuation_bytes = 0

    for byte in data:
        if expected_continuation_bytes == 0:
            if byte & 0x80 == 0:
                continue
            if byte & 0xE0 == 0xC0:
                expected_continuation_bytes = 1
            elif byte & 0xF0 == 0xE0:
                expected_continuation_bytes = 2
            elif byte & 0xF8 == 0xF0:
                expected_continuation_bytes = 3
            else:
                return False
        else:
            if byte & 0xC0 != 0x80:
                return False
            expected_continuation_bytes -= 1

    return expected_continuation_bytes == 0
