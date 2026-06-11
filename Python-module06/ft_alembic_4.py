#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_4.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/11 10:05:20 by andry-ha            #+#    #+#            #
#   Updated: 2026/06/11 13:07:41 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")

print("Now show that not all functions can be reached")
print("This will raise an exception!\nTesting the hidden create_earth:",
      end=" ")
print(f"{alchemy.create_earth()}")
