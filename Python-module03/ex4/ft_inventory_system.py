#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/22 15:50:43 by andry-ha            #+#    #+#            #
#   Updated: 2026/05/26 14:30:27 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


class InventorySystemError(Exception):
    pass


class NoItemsProvidedError(InventorySystemError):
    def __init__(self) -> None:
        message = "No items provided. "\
            "Usage: python3 ft_inventory_system.py"\
            " <key1:value1> <key2:value2> ..."
        super().__init__(message)


class InvalidParameterError(InventorySystemError):
    def __init__(self, parameter: str) -> None:
        message = f"Error - invalid parameter '{parameter}'"
        super().__init__(message)


class RedundantItemError(InventorySystemError):
    def __init__(self, item_name: str) -> None:
        message = f"Redundant item '{item_name}' - discarding."
        super().__init__(message)


class QuantityConversionError(InventorySystemError):
    def __init__(self, key: str) -> None:
        message = f"Quantity error for '{key}'"
        super().__init__(message)


class DivisionByZeroError(InventorySystemError):
    def __init__(self) -> None:
        message = "Division error: "
        super().__init__(message)


def get_inventory(parameters: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for param in parameters:
        if ":" not in param:
            print(InvalidParameterError(param))
            continue

        item_name, quantity_str = param.split(":")
        item_name = item_name.strip()
        quantity_str = quantity_str.strip()

        if not item_name:
            print(InvalidParameterError(param))
            continue

        if item_name in inventory:
            print(RedundantItemError(item_name))
            continue

        try:
            quantity = int(quantity_str)
            inventory[item_name] = quantity
        except ValueError as e:
            print(f"{QuantityConversionError(item_name)}: {e}")
            continue

    return inventory


def ft_inventory_system() -> dict[str, int]:
    print("=== Inventory System Analysys ===")

    try:
        parameters: list[str] = sys.argv[1:]
        if not parameters:
            raise NoItemsProvidedError()
        inventory: dict[str, int] = get_inventory(parameters)

        print(f"Got inventory: {inventory}")

        keys = list(inventory.keys())
        print(f"Item list: {keys}")

        total_values = sum(inventory.values())
        print(f"Total quantity of the {len(keys)} items: {total_values}")

        for key, value in inventory.items():
            percentage = (value / total_values) * 100
            print(f"Item {key} represents: {percentage:.1f}%")

        def get_quantity(key: str) -> int:
            return inventory[key]

        most_abondant = max(inventory, key=get_quantity)
        max_value = inventory[most_abondant]

        least_abondant = min(inventory, key=get_quantity)
        min_value = inventory[least_abondant]

        print(f"Item most abondant: {most_abondant}"
              f" with quantity {max_value}")
        print(f"Item least abondant: {least_abondant}"
              f" with quantity {min_value}")
    except NoItemsProvidedError as e:
        print(e)
        inventory = {}
    except ZeroDivisionError as e:
        print(f"{DivisionByZeroError()}: {e}")
        inventory = {}
    return inventory


if __name__ == "__main__":
    try:
        inventory = ft_inventory_system()
        inventory.update({'magic_item': 1})
        print(f"Updated inventory: {inventory}")
    except Exception as e:
        print(f"{e}")
