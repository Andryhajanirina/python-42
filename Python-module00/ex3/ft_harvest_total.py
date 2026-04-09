#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_harvest_total.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/09 12:50:48 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/09 12:50:49 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_harvest_total() -> None:
    weight_harvest_one = int(input("Day 1 harvest: "))
    weight_harvest_two = int(input("Day 2 harvest: "))
    weight_harvest_three = int(input("Day 3 harvest: "))
    total = weight_harvest_one + weight_harvest_two + weight_harvest_three
    print(f"Total harvest: {total}")
