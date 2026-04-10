#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/10 15:50:04 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/10 15:50:42 by andry-ha           ###   ########.fr      #
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
