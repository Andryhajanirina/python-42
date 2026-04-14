#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/13 14:09:38 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/13 16:01:27 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self.name = name.capitalize()
        self._height = 0.0
        self.__private_name = name
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Error: Invalid age '{age}'"
                  f" provided for {self.name}. "
                  f"Age cannot be negative.")
        else:
            self._age = age

    def set_height(self, sheight: float) -> None:
        if sheight < 0:
            print(f"Error: Invalid height '{sheight}'"
                  f" provided for {self.name}. "
                  f"Height cannot be negative.")
        else:
            self._height = sheight

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def age(self, age_growth: int) -> None:
        self._age += age_growth

    def grow(self, growth_cm: float) -> None:
        self._height += growth_cm

    def show(self, label: str = "") -> None:
        if label:
            print(f"=== {label}")
        print(
            f"Created: {self.name}: "
            f"{self._height:.1f}cm, {self._age} days old"
        )


class Flower(Plant):
    def __init__(self, name: str, color: str, height: float = 0, age: int = 0):
        self._color = color
        super().__init__(name, height, age)

    def bloom(self) -> None:
        # self.show()
        print(f"{self.name.capitalize()} is blooming beutifully")

    def show(self, label: str = "") -> None:
        super().show(self.__class__.__name__)
        print(f"Color: {self._color}")


class Tree(Plant):
    def __init__(self, name: str, trunk_diameter: float,
                 height: float = 0, age: int = 0):
        self._trunk_diameter = trunk_diameter
        super().__init__(name, height, age)

    def produce_shade() -> None:
        pass

    def show(self) -> None:
        super().show(self.__class__.__name__)
        print(f"{self.name.capitalize()} diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, harvest_season: str,
                 nutritional_value: str, height: float = 0, age: int = 0):
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value
        super().__init__(name, height, age)

    def show(self, label: str = "") -> None:
        super().show(self.__class__.__name__)
        print(f"Season: {self._harvest_season}\n"
              f"Nutritional: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", "red", 15.5, 2)
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()

    cactus = Tree("Cactus", 12.0, 5, 3)
    cactus.show()

    tomato = Vegetable("tomato", "Avril", 10.0, 20)
    tomato.show()
