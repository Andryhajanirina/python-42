#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_archive_creation.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/02 10:31:17 by andry-ha            #+#    #+#            #
#   Updated: 2026/06/07 15:56:28 by andry-ha           ###   ########.fr      #
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


def open_file(filename: str, mode: str) -> typing.IO[str]:
    try:
        return open(filename, mode)
    except (FileNotFoundError, PermissionError) as e:
        raise OpeningFileError(filename, e)


def print_separator() -> None:
    print("---")


def display_file_content(filename: str) -> str:
    file: typing.IO[str] | None = None

    try:
        mode = "r"
        source_mode = "r+" if "w" in mode else mode
        file = open_file(filename, mode=source_mode)
        content: str = file.read()

        print_separator()
        print()
        for line in content:
            print(line, end="")
        print()
        print_separator()

        return content

    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.")


def transform_lines(sources_file: typing.IO[str]) -> list[str]:
    transformed: list[str] = []

    print_separator()
    print()
    for line in sources_file:
        cleaned_line = line.rstrip("\r\n") + "#"
        transformed.append(cleaned_line)
        print(cleaned_line)
    print()
    print_separator()

    return transformed


def save_data(lines: list[str]) -> None:
    new_filename: str = input(
        "Enter new file name (or empty): "
    )

    if not new_filename:
        print("Not saving data.")
        return

    file: typing.IO[str] | None = None

    try:
        file = open_file(new_filename, "w")

        for line in lines:
            file.write(f"{line}\n")

        print(f"Saving data to '{new_filename}'")
        print(f"Data saved in file '{new_filename}'.\n")

    finally:
        if file is not None:
            file.close()


def main() -> None:
    file: typing.IO[str] | None = None
    try:
        args: list[str] = sys.argv[1:]

        if len(args) == 0:
            raise NoArgumentProvidedError()

        filename: str = args[0]

        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{filename}'")

        display_file_content(filename)

        print("\nTransform data:")

        file = open_file(filename, "r")
        transformed_lines = transform_lines(file)

        save_data(transformed_lines)

    except AncientTextError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nGood bye")
    finally:
        if file is not None:
            file.close()


if __name__ == "__main__":
    main()
