#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/11 13:35:27 by andry-ha            #+#    #+#            #
#   Updated: 2026/05/22 15:50:24 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random


ALL_POSSIBLE: list[str] = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
    "Boss Slayer"
]


def gen_player_achievements() -> set[str]:
    num_to_pick: int = random.randint(2, 5)

    return set(random.sample(ALL_POSSIBLE, num_to_pick))


if __name__ == "__main__":
    player_names: tuple[str, str, str, str] = (
        "Alice", "Bob", "Charlie", "Dylan"
    )

    all_possible_set: set[str] = set(ALL_POSSIBLE)

    achievements_alice: set[str] = gen_player_achievements()
    achievements_bob: set[str] = gen_player_achievements()
    achievements_charlie: set[str] = gen_player_achievements()
    achievements_dylan: set[str] = gen_player_achievements()

    all_players_achievements: tuple[set[str], set[str], set[str], set[str]] = (
        achievements_alice,
        achievements_bob,
        achievements_charlie,
        achievements_dylan
    )

    for i in range(len(all_players_achievements)):
        print(f"Player {player_names[i]}: {all_players_achievements[i]}")

    common: set[str] = set.intersection(*all_players_achievements)
    print(f"\nCommon achievements: {common}\n")

    all_distinct: set[str] = set.union(*all_players_achievements)
    print(f"All distinct achievements: {all_distinct}\n")

    for i in range(len(all_players_achievements)):
        current_name: str = player_names[i]
        current_set: set[str] = all_players_achievements[i]

        other_sets_list: list[set[str]] = []
        for j in range(len(all_players_achievements)):
            if i != j:
                other_sets_list.append(all_players_achievements[j])

        union_others: set[str] = set.union(*other_sets_list)
        only_this_player: set[str] = set.difference(current_set, union_others)

        print(f"Only {current_name} has: {only_this_player}")

    print()

    for i in range(len(all_players_achievements)):
        current_name = player_names[i]
        current_set = all_players_achievements[i]
        missing: set[str] = set.difference(all_possible_set, current_set)

        print(f"{current_name} is missing: {missing}")
