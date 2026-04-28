#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/10 15:50:04 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/27 10:42:27 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self.name = name.capitalize()
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name.capitalize()}: Error, "
                  f"age cannot be negative.\nAge update rejected")
        else:
            self._age = age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name.capitalize()}: Error, "
                  f"height cannot be negative.\nHeight update rejected")
        else:
            self._height = height

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
            f"Plant created: {self.name}: "
            f"{self._height:.1f}cm, {self._age} days old\n"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    rose.show()
    rose.set_height(25)
    rose.set_age(30)
    print(f"Height updated: {rose.get_height()}cm\n"
          f"Age updadated: {rose.get_age()} days\n")

    rose.set_height(-12.3)
    rose.set_age(-12)
    print(f"Current state: {rose.name.capitalize()}: "
          f"{rose.get_height():.1f}cm, {rose.get_age()} days old")
