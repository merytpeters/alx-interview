#!/usr/bin/python3
"""Log Parsing.
This module provides functions to parse log data and compute statistics.
"""
import sys
import re


class LogParser:
    """Class Log Parser"""

    def __init__(self):
        """Class initialization"""
        self.total_file_size = 0
        self.status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                                  404: 0, 405: 0, 500: 0}

    def parse_line(self, line):
        """Parse a line of log data."""
        pattern = (r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 '
                   r'HTTP/1\.1" (\d+) (\d+)$')

        match = re.match(pattern, line)
        if match:
            ip_address = match.group(1)
            date = match.group(2)
            try:
                status_code = int(match.group(3))
                file_size = int(match.group(4))
            except ValueError:
                return None
            return ip_address, date, status_code, file_size
        return None

    def print_statistics(self):
        """Print statistics."""
        print("File size:", self.total_file_size)
        for status_code in sorted(self.status_code_count.keys()):
            if self.status_code_count[status_code] > 0:
                print("{}: {}".format(status_code,
                                      self.status_code_count[status_code]))

    def process_logs(self):
        """Process log lines from standard input."""
        try:
            line_count = 0
            for line in sys.stdin:
                line_count += 1
                line = line.strip()
                parsed_data = self.parse_line(line)
                if parsed_data:
                    _, _, status_code, file_size = parsed_data
                    self.total_file_size += file_size
                    self.status_code_count[status_code] = self\
                        .status_code_count.get(status_code, 0) + 1

                # Print statistics after every 10 lines
                if line_count % 10 == 0:
                    self.print_statistics()
            self.print_statistics()

        except Exception:
            self.print_statistics()
            sys.exit(0)


def main():
    parser = LogParser()
    parser.process_logs()


if __name__ == "__main__":
    main()
