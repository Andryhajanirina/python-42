#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/10 15:50:04 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/13 12:57:58 by andry-ha           ###   ########.fr      #
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
            print(f"=== {label} ===")
        print(
            f"Created: {self.name}: "
            f"{self._height:.1f}cm, {self._age} days old"
        )


if __name__ == "__main__":
    print("--- Test 1 : With valid values ---")
    rose = Plant("Rose", 15.5, 2)
    rose.show("Show Rose info")
    print(f"Plant : {rose.name}\nHeight : {rose.get_height()}\n"
          f"Age : {rose.get_age()}")

    print("\n--- Test 2 : With invalid values negative "
          "(Leaving data unchanged) ---")
    cactus = Plant("Cactus", -5.0, -1)
    cactus.show("Show Cactus info")
    print(f"Plant : {cactus.name}\nHeight : {cactus.get_height()}\n"
          f"Age : {cactus.get_age()}")

    print("\n--- Test 3 : Invalid modification attempt ---")
    rose.set_height(-12.3)
    print(f"Height after echec : {rose.get_height()}")
