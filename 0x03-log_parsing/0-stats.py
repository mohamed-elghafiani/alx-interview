#!/usr/bin/env python3
"""ALx interview
  Log parsing
"""
import sys
import re


total_size = 0
status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "402": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

for n, line in enumerate(sys.stdin):
    pattern = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        r' - ' 
        r'\[[^\]]+\]'
        r' "GET /projects/260 HTTP/1.1"'
        r' (?P<status_code>\d{3})'
        r' (?P<size>\d+)'
    )

    match = pattern.match(line)
    if match:
        total_size += int(match.groupdict()['size'])
        status_codes[match.groupdict()['status_code']] += 1
    
    if n % 10:
        print(f"File size: {total_size}")
        for key, val in status_codes.items():
            if val != 0:
                print(f"{key}: {val}")