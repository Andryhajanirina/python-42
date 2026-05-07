#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/30 13:45:40 by andry-ha            #+#    #+#            #
#   Updated: 2026/05/07 10:47:40 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def ft_command_quest():
    if len(sys.argv) > 1:
        print("=== Command Quest ===")
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {len(sys.argv)}")
    else:
        print("=== Command Quest ===")
        print(f"Program name: {sys.argv[0]} ")
        print("No arguments provided!")
        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()
