#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   potions.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/11 10:31:17 by andry-ha            #+#    #+#            #
#   Updated: 2026/06/11 12:47:47 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .elements import create_earth, create_air
from elements import create_fire, create_water


def healing_potion() -> str:
    return ("Healing potion brewed with" +
            f" '{create_earth()}' and '{create_air()}'")


def strength_potion() -> str:
    return ("Strength potion brewed with" +
            f" '{create_fire()}' and '{create_water()}'")
