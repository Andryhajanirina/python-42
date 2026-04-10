#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/09 14:08:53 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/10 15:54:20 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def age(self, age_growth: int) -> None:
        self.age_days += age_growth

    def grow(self, growth_cm: float) -> None:
        self.height += growth_cm

    def show(self, label: str = "") -> None:
        if label:
            print(f"=== {label} ===")
        print(
            f"{self.name.capitalize()}: "
            f"{round(self.height, 1)}cm, {self.age_days} days old"
        )


if __name__ == "__main__":
    rose = Plant("rose", 25.0, 30)
    sunflower = Plant("sunflower", 80, 45)
    initial_height = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()

    for day in range(1, 8):
        rose.age(1)
        rose.grow(0.8)
        rose.show(f"Day {day}")

    total_growth = rose.height - initial_height
    print(f"Growth this week: {round(total_growth, 1)}cm")

    print("\n**********************\n")
    print("=== Garden Plant Growth ===")
    sunflower.show()

    for day in range(1, 8):
        sunflower.age(1)
        sunflower.grow(2.1)
        sunflower.show(f"Day {day}")
