#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   recipes.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/11 10:49:28 by andry-ha            #+#    #+#            #
#   Updated: 2026/06/11 12:56:26 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ..elements import create_air
from alchemy.potions import strength_potion
from elements import create_fire


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew"
            f" '{create_air()}' and"
            f" '{strength_potion()}' mixed with"
            f" '{create_fire()}'")
