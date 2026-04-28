#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/20 15:13:18 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/28 16:44:35 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self.name = name.capitalize()
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)
        self._stats = self._Stats()

    class _Stats:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(f"Stats:"
                  f" {self.grow_calls} grow,"
                  f" {self.age_calls} age,"
                  f" {self.show_calls} show")

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls(name="Unknown plant", height=0.0, age=0)

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
        self._stats.age_calls += 1

    def grow(self, growth_cm: float) -> None:
        self._height += growth_cm
        self._stats.grow_calls += 1

    def show(self, label: str = "") -> None:
        self._stats.show_calls += 1
        if label:
            print(f"=== {label}")
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, color: str,
                 height: float = 0.0, age: int = 0):
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True
        self.show(label="")
        print(f" {self.name.capitalize()} is blooming beautifully!")

    def show(self, label: str = "") -> None:
        super().show(label)
        print(f" Color: {self._color}")
        if not self._bloomed:
            print(f" {self.name.capitalize()} has not bloomed yet")
            display_plant_stats(self)
            print(f"[asking the {self.name.lower()} to grow and bloom]")


class Seed(Flower):
    def __init__(self, name: str, color: str,
                 seeds: int = 0, height: float = 0.0, age: int = 0) -> None:
        super().__init__(name, color, height, age)
        self.seeds = seeds

    def bloom(self) -> None:
        self._bloomed = True
        self.grow(30)
        self.age(20)
        self.show()
        print(f" {self.name.capitalize()} is blooming beautifully!")
        print(f" Seeds: {self.seeds}")

    def show(self, label: str = "") -> None:
        if label:
            print(f"=== {label}")
        Plant.show(self)
        print(f" Color: {self._color}")
        if not self._bloomed:
            print(f" {self.name.capitalize()} has not bloomed yet")
            print(f" Seeds: {self.seeds}")
            print("[make sunflower grow, age and bloom]")


class Tree(Plant):
    class _Stats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(self, name: str, trunk_diameter: float,
                 height: float = 0.0, age: int = 0) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._provide_shade = False
        self._stats: Tree._Stats = self._Stats()

    def produce_shade(self) -> None:
        self._stats._shade_calls += 1
        self._provide_shade = True
        print(f"Tree {self.name} now produces a shade of {self._height}cm long"
              f" and {self._trunk_diameter}cm wide.")
        display_plant_stats(self)

    def show(self, label: str = "") -> None:
        if not self._provide_shade:
            super().show(label)
            print(f" Trunk diameter: {self._trunk_diameter}cm")
            display_plant_stats(self)
            print("[asking the oak to produce shade]")


class Vegetable(Plant):
    def __init__(self, name: str, harvest_season: str,
                 nutritional_value: int = 0,
                 height: float = 0.0,
                 age: int = 0) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def age(self, age_growth: int) -> None:
        super().age(age_growth)
        self._nutritional_value += age_growth
        self.show(label="", should_age=True)

    def show(self, label: str = "", should_age: bool = False) -> None:
        if not should_age:
            super().show(label)
            print(f" Harvest season: {self._harvest_season}\n"
                  f" Nutritional value: {self._nutritional_value}")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    rose = Flower("Rose", "red", 15.0, 10)
    print(f"Is 30 days more than a year? -> {rose.is_older_than_year(30)}\n"
          f"Is 400 days more than a year? -> {rose.is_older_than_year(400)}\n")

    rose.show(label=rose.__class__.__name__)
    rose.grow(8)
    rose.bloom()
    display_plant_stats(rose)

    print("")

    oak = Tree("Oak", trunk_diameter=5.0, height=200.0, age=365)
    oak.show(label=oak.__class__.__name__)
    oak.produce_shade()

    print("")

    sunflower = Seed("sunflower", height=80.0, color="yellow", age=45)
    sunflower.show(label=sunflower.__class__.__name__)
    sunflower.seeds = 42
    sunflower.bloom()
    display_plant_stats(sunflower)

    print("")

    anonymous = Plant.create_anonymous()
    anonymous.show("Anonymous")
    display_plant_stats(anonymous)
