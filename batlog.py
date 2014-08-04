import os
import subprocess
import time

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
VALUE_PRECEDER = '" = '
OUTPUT_DELIMITER = ","
MATCHES = ["CycleCount", "Capacity"]
IGNORE_MATCHES = ["LegacyBatteryInfo"]
COMMAND = ["/usr/sbin/ioreg", "-l"]

logValues = []

# Read I/O registry and save output
process = subprocess.Popen(COMMAND, stdout=subprocess.PIPE)
output, error = process.communicate()

# Append the date and time
logValues.append(time.strftime(DATE_FORMAT))

# Get values from output
for line in output.split(os.linesep):
    if any(match in line for match in MATCHES) and not any(match in line for match in IGNORE_MATCHES):
        logValues.append(line[line.find(VALUE_PRECEDER) + len(VALUE_PRECEDER):])

print OUTPUT_DELIMITER.join(logValues)