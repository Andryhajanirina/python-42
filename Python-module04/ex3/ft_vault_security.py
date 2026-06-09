#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_vault_security.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/03 14:20:20 by andry-ha            #+#    #+#            #
#   Updated: 2026/06/07 16:22:01 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def secure_archive(file_name: str,
                   mode: str = "r",
                   destination: str = "") -> tuple[bool, str]:
    try:
        with open(file_name, mode) as file:
            content = file.read()

            if destination:
                with open(destination, "w") as dest_file:
                    dest_file.write(content)
                return True, "Content successfully written to file"

            return True, f"{content}"

    except FileNotFoundError as e:
        return False, f"{e}"
    except PermissionError as e:
        return False, f"{e}"
    except Exception as e:
        return False, f"{e}"


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    file_name = "/not/existing/file"
    print(f"{secure_archive(file_name=file_name)}\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    file_name = "/etc/master.passwd"
    print(f"{secure_archive(file_name=file_name, mode='w')}\n")

    print("Using 'secure_archive' to read from a regular file:")
    file_name = "ancient_fragment.txt"
    print(f"{secure_archive(file_name=file_name)}\n")

    print("Using 'secure_archive' to write previous content to a new file:")
    file_name = "ancient_fragment.txt"
    print(f"""{secure_archive(
        file_name=file_name, mode='r+', destination='destination.txt')}\n""")
