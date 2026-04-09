#!/usr/bin/env python3
def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    i = 1
    while days > 0:
        print(f"Days {i}")
        i += 1
        days -= 1
    print("Harvest time!")
