#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_pipeline.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/08 15:47:37 by andry-ha            #+#    #+#            #
#   Updated: 2026/06/10 12:49:56 by andry-ha           ###   ########.fr      #
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


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, typing.Any]]) -> None:
        """Manually generates a CSV line containing only the values."""
        values = [str(item_val) for _, item_val in data]

        csv_line = ",".join(values)
        print("CSV Output:")
        print(csv_line)


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, typing.Any]]) -> None:
        """Manually generates a JSON dictionary in the format {"item_id": "value"}."""
        json_parts = []
        for item_id, item_val in data:
            escaped_val = str(item_val).replace('"', '\\"')
            json_parts.append(f'"item_{item_id}": "{escaped_val}"')

        # Assemblage sous forme d'une ligne dictionnaire JSON
        json_output = "{" + ", ".join(json_parts) + "}"
        print("JSON Output:")
        print(json_output)


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
        print("\n== DataStream statistics ==")
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
        """Consomme jusqu'à nb éléments pour CHAQUE processeur individuellement

        et déclenche l'affichage du plugin à chaque fois.
        """
        for processor in self.processors:
            processor_data: list[tuple[int, typing.Any]] = []

            # Consommer au maximum 'nb' éléments restants pour ce processeur
            for _ in range(nb):
                if hasattr(processor, '_storage')\
                   and len(processor._storage) == 0:
                    break

                item = processor.output()
                if isinstance(item, tuple) and len(item) == 2:
                    processor_data.append(item)

            if processor_data:
                plugin.process_output(processor_data)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")

    stream_manager = DataStream()
    stream_manager.print_processors_stats()

    print("\nRegistering Processors\n")
    num_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()

    stream_manager.register_processor(num_processor)
    stream_manager.register_processor(text_processor)
    stream_manager.register_processor(log_processor)

    batch1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]

    print(f"Send first batch of data on stream: {batch1}")
    stream_manager.process_stream(batch1)
    stream_manager.print_processors_stats()

    # --- FIRST EXPORT : CSV ---
    csv_plugin = CSVExportPlugin()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream_manager.output_pipeline(nb=3, plugin=csv_plugin)

    stream_manager.print_processors_stats()

    # --- SECOND BATCH ---
    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {
                'log_level': 'ERROR',
                'log_message': '500 server crash'
            },
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print(f"\nSend another batch of data: {batch2}")
    stream_manager.process_stream(batch2)
    stream_manager.print_processors_stats()

    # --- SECOND EXPORT : JSON ---
    json_plugin = JSONExportPlugin()
    print("Send 5 processed data from each processor to a JSON plugin:")
    stream_manager.output_pipeline(nb=5, plugin=json_plugin)

    stream_manager.print_processors_stats()
