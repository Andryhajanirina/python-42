#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/10 14:01:56 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/10 15:49:18 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
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
            f"Created: {self.name}: "
            f"{self.height:.1f}cm, {self.age_days} days old"
        )


if __name__ == "__main__":
    rose = Plant("rose", 25.0, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)
    tomato = Plant("tomato", 10.0, 20)
    apple = Plant("apple", 200, 365)
    my_plants = [rose, sunflower, cactus, tomato, apple]
    print("=== Plant Factory Output ===")
    for plant in my_plants:
        plant.show()
