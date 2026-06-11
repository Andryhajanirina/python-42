#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   light_validator.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/11 11:27:21 by andry-ha            #+#    #+#            #
#   Updated: 2026/06/11 12:55:14 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    for ingredient in allowed:
        if ingredient in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
