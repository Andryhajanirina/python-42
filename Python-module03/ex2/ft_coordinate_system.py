#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/07 10:49:39 by andry-ha            #+#    #+#            #
#   Updated: 2026/05/11 13:32:42 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import math


class PositionTrackerError(Exception):
    pass


class NoCoordinatesProvidedError(PositionTrackerError):
    def __init__(self) -> None:
        message = "No coordinates provided."
        super().__init__(message)


class NonNumericCoordinatesError(PositionTrackerError):
    def __init__(self, coordinates: str) -> None:
        message = (f"Error on parameter '{coordinates}': "
                   f"could not convert string to float: '{coordinates}'")
        super().__init__(message)


class InvalidCoordinatesError(PositionTrackerError):
    def __init__(self) -> None:
        message = "Invalid syntax"
        super().__init__(message)


def distance_3d(point_a: tuple[float, float, float],
                ppoint_b: tuple[float, float, float]) -> float:
    x1, y1, z1 = point_a
    x2, y2, z2 = ppoint_b

    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )


def get_player_pos() -> tuple[float, float, float]:
    entries = input(
        "Enter new coordinates as floats in format 'x,y,z': "
    ).strip()

    if not entries:
        raise InvalidCoordinatesError()

    parts = entries.split(",")

    if len(parts) != 3:
        raise InvalidCoordinatesError()

    try:
        x: float = float(parts[0].strip())
        y: float = float(parts[1].strip())
        z: float = float(parts[2].strip())
        return (x, y, z)
    except ValueError:
        for coordinate_str in parts:
            try:
                float(coordinate_str)
            except ValueError:
                raise NonNumericCoordinatesError(coordinate_str)
        raise InvalidCoordinatesError()


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    center_pos = (0.0, 0.0, 0.0)

    print("Get a first set of coordinates")
    while True:
        try:
            first_pos = get_player_pos()
            break
        except PositionTrackerError as e:
            print(e)

    print(f"Got a first tuple: {first_pos}")
    print(f"It includes: X={first_pos[0]}, Y={first_pos[1]}, Z={first_pos[2]}")
    print(f"Distance to center: {distance_3d(center_pos, first_pos):.4f}")

    print("\nGet a second set of coordinates")
    while True:
        try:
            second_pos = get_player_pos()
            break
        except PositionTrackerError as e:
            print(e)

    print(f"Distance between the 2 sets of coordinates: "
          f"{distance_3d(first_pos, second_pos):.4f}")
