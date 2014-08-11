import os
from os.path import dirname, abspath

from batlog import BatlogPython


baseDir = dirname(abspath(__file__)) + os.path.sep

IOREG_DATA_FILE_PATH = "data" + os.path.sep + "ioreg_partial_output"


def test_that_correct_data_is_parsed():
    with open(baseDir + IOREG_DATA_FILE_PATH) as data_file:
        registry_contents = data_file.read()

    batlog_python = BatlogPython(registry_contents, "\n")
    batlog_python.set_log_entry()

    assert batlog_python.COLUMN_NAME_DATE in batlog_python.log_entry.keys()
    assert batlog_python.COLUMN_NAME_CYCLE_COUNT in batlog_python.log_entry.keys()
    assert batlog_python.COLUMN_NAME_MAXIMUM_CAPACITY in batlog_python.log_entry.keys()
    assert batlog_python.COLUMN_NAME_CURRENT_CAPACITY in batlog_python.log_entry.keys()
    assert batlog_python.COLUMN_NAME_DESIGN_CAPACITY in batlog_python.log_entry.keys()

    assert batlog_python.log_entry[batlog_python.COLUMN_NAME_CYCLE_COUNT] == "158"
    assert batlog_python.log_entry[batlog_python.COLUMN_NAME_MAXIMUM_CAPACITY] == "8181"
    assert batlog_python.log_entry[batlog_python.COLUMN_NAME_CURRENT_CAPACITY] == "3188"
    assert batlog_python.log_entry[batlog_python.COLUMN_NAME_DESIGN_CAPACITY] == "8440"