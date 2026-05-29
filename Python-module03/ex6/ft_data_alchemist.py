#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_alchemist.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/29 10:05:57 by andry-ha            #+#    #+#            #
#   Updated: 2026/05/29 11:15:47 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random


def main() -> None:
    players: list[str] = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"
    ]

    capitalized_names: list[str] = [name.capitalize() for name in players]
    only_capitalized_name: list[str] = [
        name for name in players if name == name.capitalize()
    ]

    score_dict: dict[str, int] = {
        name: random.randint(1, 999) for name in capitalized_names
    }
    average: float = (sum(score_dict.values()) / len(score_dict))
    high_scores: dict[str, int] = {
        name: score for name, score in score_dict.items() if score > average
    }
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capitalized_names}")
    print(f"New list of capitalized names only: {only_capitalized_name}\n")
    print(f"Score dict: {score_dict}")
    print(f"Score average is {round(average, 2)}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
