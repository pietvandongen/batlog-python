import os
import subprocess
import sys
import time

from collections import OrderedDict

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

# Get output file name
try:
    outputFile = str(sys.argv[1])
except IndexError:
    print "Error: please provide an output file name"
    sys.exit(2)

# Read I/O registry and save output
process = subprocess.Popen(COMMAND, stdout=subprocess.PIPE)
logContents, error = process.communicate()

# Append the date and time
logEntry["Date"] = time.strftime(DATE_FORMAT)

# Get values from log
for line in logContents.split(os.linesep):
    if any(match in line for match in MATCHES):
        key = line[line.find(KEY_DELIMITER) + len(KEY_DELIMITER):line.find(VALUE_DELIMITER)]
        value = line[line.find(VALUE_DELIMITER) + len(VALUE_DELIMITER):]

        if key in COLUMNS:
            logEntry[key] = value

OUTPUT_HEADER = OUTPUT_DELIMITER.join(logEntry.keys()) + "\n"

# Check if the output file has the correct header
if os.path.isfile(outputFile):
    with open(outputFile, 'r') as openFile:
        fileHasHeader = (openFile.readline() == OUTPUT_HEADER)

# Write to file
with open(outputFile, 'a+') as openFile:
    if not fileHasHeader:
        openFile.write(OUTPUT_HEADER)

    openFile.write(OUTPUT_DELIMITER.join(logEntry.values()) + "\n")
