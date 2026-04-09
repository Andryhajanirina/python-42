#!/usr/bin/env python3
def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def _helper(days: int, current_days: int = 1) -> None:
        if days <= 0:
            print("Harvest time!")
        else:
            print(f"Days {current_days}")
            _helper(days - 1, current_days + 1)
    _helper(days)
