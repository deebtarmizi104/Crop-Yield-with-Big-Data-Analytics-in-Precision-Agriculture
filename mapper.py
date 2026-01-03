#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    fields = line.split(",")

    try:
        key = fields[1].strip()          # example: soil type (Sandy/Clay/Loam)
        days = float(fields[8])          # days_to_harvest
        rain = float(fields[9])          # rainfall
        temp = float(fields[4])          # temperature  (CHANGE if needed)
        yld  = float(fields[3])          # yield
        c    = 1.0                       # count
    except:
        continue

    print(f"{key}\t{days},{rain},{temp},{yld},{c}")
