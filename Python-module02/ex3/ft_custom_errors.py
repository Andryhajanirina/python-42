#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/27 14:57:43 by andry-ha            #+#    #+#            #
#   Updated: 2026/05/07 10:45:01 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    """A fundamental error for the entire garden."""
    pass


class PlantError(GardenError):
    def __init__(self, plant_name: str = "Unknown"):
        self.plant_name = plant_name
        message: str = f"The {self.plant_name} plant is wilting!"
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!"):
        super().__init__(message)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    try:
        raise PlantError("tomato")
    except PlantError as e:
        print("Testing PlantError...")
        print(f"Caught PlantError: {e}\n")

    try:
        raise WaterError()
    except WaterError as e:
        print("Testing WaterError...")
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    all_errors = [PlantError("tomato"), WaterError()]

    for error in all_errors:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")
