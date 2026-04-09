#!/usr/bin/env python3
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seeds = f"{seed_type} seeds: "
    if unit == "packets":
        seeds += f"{quantity} packets available"
    elif unit == "grams":
        seeds += f"{quantity} grams total"
    elif unit == "area":
        seeds += f"covers {quantity} square meters"
    else:
        seeds = "Unknown unit type"
    print(f"{seeds.capitalize()}")
