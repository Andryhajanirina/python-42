#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/30 13:45:40 by andry-ha            #+#    #+#            #
#   Updated: 2026/05/22 15:46:48 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


class CommandQuestError(Exception):
    pass


class NoArgumentProvidedError(CommandQuestError):
    def __init__(self) -> None:
        message: str = ("No arguments provided!")
        super().__init__(message)


def ft_command_quest() -> None:
    print("=== Command Quest ===")

    try:
        arguments_list: list[str] = sys.argv
        program_name: str = arguments_list[0]
        total_arguments: int = len(arguments_list)

        print(f"Program name: {program_name}")

        if total_arguments > 1:
            print(f"Arguments received: {total_arguments - 1}")
            for i in range(1, total_arguments):
                print(f"Argument {i}: {arguments_list[i]}")
        else:
            raise NoArgumentProvidedError()
    except NoArgumentProvidedError as e:
        print(e)
    finally:
        print(f"Total arguments: {total_arguments}\n")


if __name__ == "__main__":
    ft_command_quest()
