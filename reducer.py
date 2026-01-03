#!/usr/bin/env python3
import sys

current_region = None
sum_days = sum_rain = sum_temp = sum_yield = count = 0

for line in sys.stdin:
    region, values = line.strip().split("\t")
    days, rain, temp, yld, c = map(float, values.split(","))

    if current_region and current_region != region:
        print(f"{current_region}\t"
              f"{sum_days/count:.2f}\t"
              f"{sum_rain/count:.2f}\t"
              f"{sum_temp/count:.2f}\t"
              f"{sum_yield/count:.2f}")
        sum_days = sum_rain = sum_temp = sum_yield = count = 0

    current_region = region
    sum_days += days
    sum_rain += rain
    sum_temp += temp
    sum_yield += yld
    count += c

if current_region:
    print(f"{current_region}\t"
          f"{sum_days/count:.2f}\t"
          f"{sum_rain/count:.2f}\t"
          f"{sum_temp/count:.2f}\t"
          f"{sum_yield/count:.2f}")
