#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_seed_inventory.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/09 12:53:18 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/09 12:53:21 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seeds = f"{seed_type} seeds: "
    if unit == "packets":
        seeds += f"{quantity} packets available"
    elif unit == "grams":
        seeds += f"{quantity} grams total"
    elif unit == "area":
        seeds += f"covers {quantity} square meters"
    else:
        seeds = "Unknown unit type"
    print(f"{seeds.capitalize()}")
