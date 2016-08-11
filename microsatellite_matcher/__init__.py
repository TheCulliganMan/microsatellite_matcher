#/usr/bin/env python
from __future__ import print_function

import sys

from marker_parser import get_markers, parse_markers, split_every
from match_by_microsat import match_by_microsat
from sheet_reader import get_workbook_dicts, go_by_row


def match(file_name, individual_key="Lab ID"):
    try:
        keys, row_dicts = get_workbook_dicts(file_name)
        markers = get_markers(keys)
        processed_row_dicts = parse_markers(markers, row_dicts)
        print("\nREAD {} SUCCESSFULLY!!!".format(file_name))
        print("RESULTS:")
        match_by_microsat(
            processed_row_dicts,
            markers,
            individual_key=individual_key
        )
        print("\nDONE.")
    except AssertionError:
        print("\nFailed to read {}, it is an excel to python issue. \
        \nCopy your data to a new document and it will probably work...\
        \n\nsorry.".format(file_name))


def main():

    file_names = sys.argv[1:]
    for file_name in file_names:
        print("\n\nTrying To Read: {}".format(file_name))
        try:
            keys, row_dicts = get_workbook_dicts(file_name)
            markers = get_markers(keys)
            processed_row_dicts = parse_markers(markers, row_dicts)
            print("\nREAD {} SUCCESSFULLY!!!".format(file_name))
            print("RESULTS:")
            match_by_microsat(processed_row_dicts, markers)
            print("\nDONE.")
        except AssertionError:
            print("\nFailed to read {}, it is an excel to python issue. \
            \nCopy your data to a new document and it will probably \
            work...\n\nsorry.".format(file_name))

if __name__ == "__main__":
    main()
