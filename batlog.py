import os
import subprocess
import sys
import time


class BatlogPython:
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    KEY_DELIMITER = '"'
    VALUE_DELIMITER = '" = '
    OUTPUT_DELIMITER = ","
    MATCHES = ["CycleCount", "Capacity"]
    COMMAND = ["/usr/sbin/ioreg", "-l"]

    COLUMN_NAME_DATE = "Date"
    COLUMN_NAME_CYCLE_COUNT = "CycleCount"
    COLUMN_NAME_MAXIMUM_CAPACITY = "MaxCapacity"
    COLUMN_NAME_CURRENT_CAPACITY = "CurrentCapacity"
    COLUMN_NAME_DESIGN_CAPACITY = "DesignCapacity"

    COLUMNS = [
        COLUMN_NAME_DATE,
        COLUMN_NAME_CYCLE_COUNT,
        COLUMN_NAME_MAXIMUM_CAPACITY,
        COLUMN_NAME_CURRENT_CAPACITY,
        COLUMN_NAME_DESIGN_CAPACITY
    ]

    log_entry = {}
    registry_contents = ""
    line_separator = os.linesep

    def __init__(self, registry_contents, line_separator = os.linesep):
        self.registry_contents = registry_contents

        if line_separator:
            self.line_separator = line_separator

    def set_log_entry(self):
        self.log_entry["Date"] = time.strftime(self.DATE_FORMAT)

        for line in self.registry_contents.split(self.line_separator):
            if any(match in line for match in self.MATCHES):
                key = line[line.find(self.KEY_DELIMITER) + len(self.KEY_DELIMITER):line.find(self.VALUE_DELIMITER)]
                value = line[line.find(self.VALUE_DELIMITER) + len(self.VALUE_DELIMITER):]

                if key in self.COLUMNS:
                    self.log_entry[key] = value

    def write_log_entry(self, output_file_path):
        header = self.OUTPUT_DELIMITER.join(self.log_entry.keys()) + "\n"
        file_has_header = False

        if os.path.isfile(output_file_path):
            with open(output_file_path, 'r') as openFile:
                file_has_header = (openFile.readline() == header)

        with open(output_file_path, 'a+') as openFile:
            if not file_has_header:
                openFile.write(header)

            openFile.write(self.OUTPUT_DELIMITER.join(self.log_entry.values()) + "\n")


def main():
    try:
        output_file_path = str(sys.argv[1])
    except IndexError:
        print "Error: please provide an output file name"
        sys.exit(2)

    process = subprocess.Popen(BatlogPython.COMMAND, stdout=subprocess.PIPE)
    registry_contents, error = process.communicate()

    batlog_python = BatlogPython(registry_contents)
    batlog_python.set_log_entry()
    batlog_python.write_log_entry(output_file_path)


if __name__ == "__main__":
    main()
