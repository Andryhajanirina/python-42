#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_stream.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/26 14:40:43 by andry-ha            #+#    #+#            #
#   Updated: 2026/05/29 13:00:05 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Generator
import random


players: list[str] = ["Alice", "Bob", "Charlie", "Diana"]

actions: list[str] = ["run", "eat", "sleep", "code", "play", "read", "write",
                      "jump", "swim", "fly"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player: str = random.choice(players)
        action: str = random.choice(actions)
        yield (player, action)


def main() -> None:
    event_generator = gen_event()
    print("=== Game Data Stream Processor ===")

    for i in range(100):
        player, action = next(event_generator)
        print(f"Event {i}: Player '{player}' did action '{action}'")

    events_list: list[tuple[str, str]] = []
    for i in range(10):
        events_list.append(next(event_generator))
    print(f"Built list of 10 events: {events_list}")

    for player, action in consume_event(events_list):
        print(f"Got event from list: ('{player}', '{action}')")
        print("=======================")
        print(f"Remains in list: {events_list}")


def consume_event(
        target_list: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    """Consumes the list by extracting
    and removing one element at random."""
    while target_list:
        random_index: int = random.randrange(len(target_list))
        removed_event: tuple[str, str] = target_list.pop(random_index)
        yield removed_event


if __name__ == "__main__":
    main()
