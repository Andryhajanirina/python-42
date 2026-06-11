#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   dark_validator.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/11 11:37:32 by andry-ha            #+#    #+#            #
#   Updated: 2026/06/11 12:55:09 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    for ingredient in allowed:
        if ingredient in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
