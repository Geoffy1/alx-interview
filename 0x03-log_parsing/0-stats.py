#!/usr/bin/env python3

import sys
from collections import defaultdict

total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            ip_address = parts[0]
            date = parts[3].strip('[]')
            request = parts[5]
            status_code = int(parts[6])
            file_size = int(parts[7])
        except:
            # If the line doesn't match the expected format, skip it
            continue
        
        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1
        
        if line_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_code_counts.keys()):
                print(f"{code}: {status_code_counts[code]}")
        
except KeyboardInterrupt:
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")
