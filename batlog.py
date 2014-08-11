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
    COLUMNS = [
        "Date",
        "CycleCount",
        "MaxCapacity",
        "CurrentCapacity",
        "DesignCapacity"
    ]

    fileHasHeader = False
    logEntry = {}

    def __init__(self):
        # Get output file name
        try:
            outputFile = str(sys.argv[1])
        except IndexError:
            print "Error: please provide an output file name"
            sys.exit(2)

        # Read I/O registry and save output
        process = subprocess.Popen(BatlogPython.COMMAND, stdout=subprocess.PIPE)
        logContents, error = process.communicate()

        # Append the date and time
        self.logEntry["Date"] = time.strftime(self.DATE_FORMAT)

        # Get values from log
        for line in logContents.split(os.linesep):
            if any(match in line for match in self.MATCHES):
                key = line[line.find(self.KEY_DELIMITER) + len(self.KEY_DELIMITER):line.find(self.VALUE_DELIMITER)]
                value = line[line.find(self.VALUE_DELIMITER) + len(self.VALUE_DELIMITER):]

                if key in self.COLUMNS:
                    self.logEntry[key] = value

        OUTPUT_HEADER = self.OUTPUT_DELIMITER.join(self.logEntry.keys()) + "\n"

        # Check if the output file has the correct header
        if os.path.isfile(outputFile):
            with open(outputFile, 'r') as openFile:
                fileHasHeader = (openFile.readline() == OUTPUT_HEADER)

        # Write to file
        with open(outputFile, 'a+') as openFile:
            if not fileHasHeader:
                openFile.write(OUTPUT_HEADER)

            openFile.write(self.OUTPUT_DELIMITER.join(self.logEntry.values()) + "\n")


def main():
    BatlogPython()


if __name__ == "__main__":
    main()
