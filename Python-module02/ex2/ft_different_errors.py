#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_different_errors.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/27 14:22:40 by andry-ha            #+#    #+#            #
#   Updated: 2026/04/27 14:56:39 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def garden_operations(operation_number: int):
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("not_exist.txt", "r")
    elif operation_number == 3:
        5 + "fleurs"


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for data in range(5):
        print(f"Testing operation {data}...")
        try:
            garden_operations(data)
        except ValueError as e:
            print(f"Caught ValueError: {e}\n")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}\n")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}\n")
        except TypeError as e:
            print(f"Caught TypeError: {e}\n")
    print("Operation completed successfully\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
