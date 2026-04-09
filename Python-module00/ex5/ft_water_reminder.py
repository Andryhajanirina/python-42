#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/09 12:52:46 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/09 12:52:47 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_water_reminder() -> None:
    last_watering = int(input("Days since last watering: "))
    if last_watering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
