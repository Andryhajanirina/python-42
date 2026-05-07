#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_finally_block.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 15:29:14 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/29 16:03:23 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    """A fundamental error for the entire garden."""
    pass


class PlantError(GardenError):
    def __init__(self, plant_name: str = "Unknown"):
        self.plant_name = plant_name
        message: str = f"{self.plant_name}"
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    # On vérifie si le nom est déjà capitalisé
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return  # Sortie immédiate
    finally:
        # Ce bloc s'exécutera TOUJOURS, même après le return ci-dessus
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])

    print("\nTesting invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])

    print("\nCleanup always happens, even with errors!")
