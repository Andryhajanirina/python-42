#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_ancient_text.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/29 13:35:17 by andry-ha            #+#    #+#            #
#   Updated: 2026/06/02 10:23:09 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import typing


class AncientTextError(Exception):
    pass


class NoArgumentProvidedError(AncientTextError):
    def __init__(self) -> None:
        message: str = "Usage: ft_ancient_text.py <file>\n"
        super().__init__(message)


class OpeningFileError(AncientTextError):
    def __init__(self, filename: str, original_error: Exception) -> None:
        self.original_error = original_error
        super().__init__(
            f"Error opening file '{filename}': {original_error}\n"
        )


def main() -> None:
    try:
        args: list[str] = sys.argv[1:]
        if len(args) == 0:
            raise NoArgumentProvidedError()
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{args[0]}'")
        filename: str = args[0]

        file: typing.IO[str] | None = None
        try:
            file = open(filename, 'r')
            content: str = file.read()
            print("---\n")
            print(content)
            print("\n---")
        except (FileNotFoundError, PermissionError) as e:
            raise OpeningFileError(filename, e)
        finally:
            if file is not None:
                file.close()
                print(f"File '{filename}' closed.")
    except NoArgumentProvidedError as e:
        print(f"{e}")
    except AncientTextError as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
