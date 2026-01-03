#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split(",")

    # Defensive check (optional but good)
    if len(fields) < 5:
        continue

    region = fields[0]
    days = float(fields[1])
    rainfall = float(fields[2])
    temp = float(fields[3])
    yield_val = float(fields[4])

    print(f"{region}\t{days},{rainfall},{temp},{yield_val},1")
