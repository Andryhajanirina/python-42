#!/usr/bin/env python3
def ft_harvest_total() -> None:
    weight_harvest_one = int(input("Day 1 harvest: "))
    weight_harvest_two = int(input("Day 2 harvest: "))
    weight_harvest_three = int(input("Day 3 harvest: "))
    total = weight_harvest_one + weight_harvest_two + weight_harvest_three
    print(f"Total harvest: {total}")
