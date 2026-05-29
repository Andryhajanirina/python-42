#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/27 14:57:43 by andry-ha            #+#    #+#            #
#   Updated: 2026/05/19 09:31:55 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    """A fundamental error for the entire garden."""
    pass


class PlantError(GardenError):
    def __init__(self, plant_name: str = "Unknown"):
        self.plant_name = plant_name
        if plant_name == "Unknown":
            message: str = "Unknown plant error"
        else:
            message = f"The {self.plant_name} plant is wilting!"
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = ""):
        if not message:
            message = "Unknown water error"
        super().__init__(message)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    try:
        raise PlantError(plant_name="tomato")
    except PlantError as e:
        print("Testing PlantError...")
        print(f"Caught PlantError: {e}\n")

    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print("Testing WaterError...")
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    all_errors = [PlantError(plant_name="tomato"),
                  WaterError(message="Not enough water in the tank!")]

    for error in all_errors:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")
