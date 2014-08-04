import os
import subprocess
import sys
import time

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
VALUE_DELIMITER = '" = '
OUTPUT_DELIMITER = ","
OUTPUT_HEADER = "Date,DesignCycleCount70,CycleCount,DesignCycleCount9C,MaxCapacity,CurrentCapacity,DesignCapacity\n"
MATCHES = ["CycleCount", "Capacity"]
IGNORE_MATCHES = ["LegacyBatteryInfo"]
COMMAND = ["/usr/sbin/ioreg", "-l"]

logValues = []
fileHasHeader = False

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
logValues.append(time.strftime(DATE_FORMAT))

# Get values from log
for line in logContents.split(os.linesep):
    if any(match in line for match in MATCHES) and not any(match in line for match in IGNORE_MATCHES):
        logValues.append(line[line.find(VALUE_DELIMITER) + len(VALUE_DELIMITER):])

# Check if the output file has the correct header
if os.path.isfile(outputFile):
    with open(outputFile, 'r') as file:
        fileHasHeader = (file.readline() == OUTPUT_HEADER)

# Write to file
with open(outputFile, 'a+') as file:
    if not fileHasHeader:
        file.write(OUTPUT_HEADER)

    file.write(OUTPUT_DELIMITER.join(logValues) + "\n")