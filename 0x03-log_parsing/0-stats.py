#!/usr/bin/python3
"""Script that reads from standard input line by line and computes
the standard metrics"""


import sys
import re
from collections import defaultdict

def process_line(line, metrics):
    """Regular expression to match the log format"""
    pattern = r'^(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - \[(?P<date>[^\]]+)\] "GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)$'
    match = re.match(pattern, line)
    
    if match:
        status_code = match.group('status')
        file_size = int(match.group('size'))
        
        # Update metrics
        metrics['total_size'] += file_size
        if status_code in metrics['status_codes']:
            metrics['status_codes'][status_code] += 1
        else:
            metrics['status_codes'][status_code] = 1

def print_metrics(metrics):
    print(f'Total file size: {metrics["total_size"]}')
    
    # Print status codes in ascending order
    for code in sorted(metrics['status_codes']):
        print(f'{code}: {metrics["status_codes"][code]}')

def main():
    metrics = {
        'total_size': 0,
        'status_codes': defaultdict(int)
    }
    line_count = 0

    try:
        for line in sys.stdin:
            process_line(line.strip(), metrics)
            line_count += 1

            if line_count % 10 == 0:
                print_metrics(metrics)

    except KeyboardInterrupt:
        print("\nKeyboard interruption received.")
        print_metrics(metrics)

if __name__ == "__main__":
    main()
