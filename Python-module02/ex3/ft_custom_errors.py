#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/27 14:57:43 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/27 16:02:51 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    def __init__(self, plant_name: str = "Unknown"):
        self.plant_name = plant_name
        message: str = f"The {self.plant_name} plant is wilting!"
        super().__init__(message)


class WatterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!"):
        super().__init__(message)


if __name__ == "__main__":
    try:
        raise PlantError("Rose")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        raise WatterError()
    except WatterError as e:
        print(f"Caught WatterError: {e}")

    try:
        raise GardenError()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
