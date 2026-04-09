#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/09 12:52:57 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/09 12:52:58 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    i = 1
    while days > 0:
        print(f"Days {i}")
        i += 1
        days -= 1
    print("Harvest time!")
