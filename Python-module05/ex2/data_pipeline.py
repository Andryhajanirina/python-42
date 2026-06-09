#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_pipeline.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/08 15:47:37 by andry-ha            #+#    #+#            #
#   Updated: 2026/06/08 16:02:37 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import abc
import typing


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


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        """Analyse chaque élément et l'envoie au processeur adéquat
        via validate()."""
        for element in stream:
            routed = False
            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    routed = True
                    break

            if not routed:
                print(f"DataStream error - "
                      f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            name_map = {
                "NumericProcessor": "Numeric Processor",
                "TextProcessor": "Text Processor",
                "LogProcessor": "Log Processor"
            }

            name = name_map.get(proc.__class__.__name__,
                                proc.__class__.__name__)
            total = proc._counter - 1
            remaining = len(proc._storage)
            print(f"{name}: total {total} items processed,"
                  f" remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        pass
