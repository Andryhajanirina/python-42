#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_transmutation_0.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/11 10:47:57 by andry-ha            #+#    #+#            #
#   Updated: 2026/06/11 12:43:33 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.transmutation.recipes

print("=== Transmutation 0 ===")
print("Using file alchemy/transmutation/recipes.py directly")
print(
    "Testing lead to gold:",
    f"{alchemy.transmutation.recipes.lead_to_gold()}\n"
    )
