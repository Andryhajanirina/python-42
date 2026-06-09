#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_processor.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/03 16:09:33 by andry-ha            #+#    #+#            #
#   Updated: 2026/06/08 13:54:32 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._counter: int = 1

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available in the processor.")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True

        if isinstance(data, list):
            if len(data) == 0:
                return False
            return all(
                isinstance(item, (int, float)) and not isinstance(item, bool)
                for item in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError(" Got exception: Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._storage.append((self._counter, str(item)))
                self._counter += 1
        else:
            self._storage.append((self._counter, str(data)))
            self._counter += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (str)):
            return True

        if isinstance(data, list):
            if len(data) == 0:
                return False
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Invalid data type for TextProcessor.")

        if isinstance(data, list):
            for item in data:
                self._storage.append((self._counter, item))
                self._counter += 1
        else:
            self._storage.append((self._counter, data))
            self._counter += 1


class LogProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:

        def is_valid_dict(d: typing.Any) -> bool:
            return isinstance(d, dict) and all(
                isinstance(k, str) and isinstance(v, str) for k, v in d.items()
            )

        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            if len(data) == 0:
                return False
            return all(is_valid_dict(item) for item in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Got exception: Improper log data")

        def format_log(log_dict: dict[str, str]) -> str:
            return ": ".join(log_dict.values())

        if isinstance(data, list):
            for item in data:
                self._storage.append((self._counter, format_log(item)))
                self._counter += 1
        else:
            self._storage.append((self._counter, format_log(data)))
            self._counter += 1


if __name__ == "__main__":
    numeric_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")

    print(f" Trying to validate input '42': {numeric_proc.validate(42)}")
    print(f" Trying to validate input 'Hello':"
          f"{numeric_proc.validate('Hello')}")

    try:
        print(" Test invalid ingestion of string 'foo'"
              " without prior validation: ")
        numeric_proc.ingest('foo')  # type: ignore[arg-type]
    except TypeError as e:
        print(e)

    try:
        data_num: list[int | float] = [1, 2, 3, 4, 5]
        print(f" Processing data: {data_num}")
        if numeric_proc.validate(data_num):
            numeric_proc.ingest(data_num)
            print(" Extracting 3 values...")
            for i in range(3):
                rank, val = numeric_proc.output()
                print(f" Numeric value {i}: {val}")
    except TypeError as e:
        print(e)
    finally:
        print()

    print("Testing Text Processor...")
    print(f" Trying to validate input '42': {text_proc.validate(42)}")

    try:
        text_data = ['Hello', 'Nexus', 'World']
        print(f" Processing data: {text_data}")

        if text_proc.validate(text_data):
            text_proc.ingest(text_data)
            i = 0
            print(" Extracting 1 values...")
            for i in range(1):
                rank, val = text_proc.output()
                print(f" Text value {i}: {val}")
    except TypeError as e:
        print(e)
    finally:
        print()

    print("Testing Log Processor...")
    print(f" Trying to validate input 'Hello': {log_proc.validate('Hello')}")

    processing_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f" Processing data: {processing_data}")
    if log_proc.validate(processing_data):
        log_proc.ingest(processing_data)
        print(" Extracting 2 values...")
        for i in range(2):
            rank, val = log_proc.output()
            print(f" Log entry {i}: {val}")
