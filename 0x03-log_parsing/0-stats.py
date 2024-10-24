#!/usr/bin/python3
"""Log Parsing.
This module provides functions to parse log data and compute statistics.
"""
import sys
import re
import signal


class LogParser:
    def __init__(self):
        """Class initialization"""
        self.total_file_size = 0
        self.status_code_count = {}

    def parse_line(self, line):
        """Parse a line of log data."""
        pattern = (r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 '
                   r'HTTP/1\.1" (\d+) (\d+)$')

        match = re.match(pattern, line)
        if match:
            ip_address = match.group(1)
            date = match.group(2)
            status_code = int(match.group(3))
            file_size = int(match.group(4))
            return ip_address, date, status_code, file_size
        return None

    def print_statistics(self):
        """Print statistics."""
        print("File size:", self.total_file_size)
        for status_code in sorted(self.status_code_count.keys()):
            print("{}: {}".format(status_code,
                                  self.status_code_count[status_code]))

    def signal_handler(self, sig, frame):
        """Handle signal interruption."""
        self.print_statistics()
        sys.exit(0)

    def process_logs(self):
        """Process log lines from standard input."""
        signal.signal(signal.SIGINT, self.signal_handler)

        try:
            for line_count, line in enumerate(sys.stdin, start=1):
                line = line.strip()
                parsed_data = self.parse_line(line)
                if parsed_data:
                    _, _, status_code, file_size = parsed_data
                    self.total_file_size += file_size
                    self.status_code_count[status_code] = self\
                        .status_code_count.get(status_code, 0) + 1

                # Print statistics after every 10 lines (or adjust as needed)
                if line_count % 10 == 0:
                    self.print_statistics()

        except (KeyboardInterrupt, BrokenPipeError):
            self.signal_handler(signal.SIGINT, None)


def main():
    parser = LogParser()
    parser.process_logs()


if __name__ == "__main__":
    main()
