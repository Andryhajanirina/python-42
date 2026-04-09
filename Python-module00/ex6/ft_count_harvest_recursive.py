#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/09 12:53:06 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/09 12:53:07 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def _helper(days: int, current_days: int = 1) -> None:
        if days <= 0:
            print("Harvest time!")
        else:
            print(f"Days {current_days}")
            _helper(days - 1, current_days + 1)
    _helper(days)
