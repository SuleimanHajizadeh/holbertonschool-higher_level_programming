#!/usr/bin/python3
"""
Skript stdin-dən gələn logları oxuyur və statistika çıxarır.

Hər 10 sətirdən sonra və ya KeyboardInterrupt zamanı:
- Total file size
- Status kodlarına görə say
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
            code = int(parts[-2])
            size = int(parts[-1])
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
