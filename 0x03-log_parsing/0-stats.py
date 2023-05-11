#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import sys
from collections import defaultdict

# Initialize variables
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        # Parse line
        try:
            parts = line.split()
            ip_address = parts[0]
            date = parts[3].strip('[]')
            request = parts[5]
            status_code = int(parts[6])
            file_size = int(parts[7])
        except:
            # Skip line if it doesn't match expected format
            continue
        
        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1
        
        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print(f"Total file size: {total_file_size}")
            for code in sorted(status_code_counts.keys()):
                print(f"{code}: {status_code_counts[code]}")
        
except KeyboardInterrupt:
    # Print final statistics on keyboard interrupt
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")

