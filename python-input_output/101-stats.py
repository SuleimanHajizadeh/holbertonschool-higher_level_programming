#!/usr/bin/python3
"""
Bu skript stdin-dən gələn logları oxuyur və hər 10 sətirdən sonra
və ya KeyboardInterrupt zamanı statistikaları çap edir.
"""

import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

total_size = 0
status_counts = {code: 0 for code in status_codes}
line_count = 0

def print_stats():
    """Statistikaları çap edir."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code]:
            print("{}: {}".format(code, status_counts[code]))

try:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        try:
            size = int(parts[-1])
            code = int(parts[-2])
        except (IndexError, ValueError):
            continue

        total_size += size
        if code in status_counts:
            status_counts[code] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    pass

print_stats()
