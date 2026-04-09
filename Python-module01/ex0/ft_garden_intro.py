#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_intro.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/09 12:49:01 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/09 13:23:43 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_garden_intro(plant: str, height: int, age: int) -> None:
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant}\nHeight: {height}cm\nAge: {age} days\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro("Rose", 25, 30)
