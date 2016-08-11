#!/usr/bin/env python
def get_markers(keys):

    markers = []
    for key in keys:
        if "@" in key:
            markers.append(key)
    return markers


def split_every(n, seq):

    seq = str(seq)
    while seq:
        int_seq = int(seq[:n])
        if int_seq == 0:
            yield -1
        else:
            yield int_seq
        seq = seq[n:]


def parse_markers(markers, row_dicts):
    for row_dict in row_dicts:

        counter = 0
        for marker in markers:
            if marker in row_dict:
                # need to support len (2)
                split_list = list(split_every(3, row_dict[marker]))
                row_dict[marker] = split_list
                counter += 1
        row_dict["marker_count"] = counter

    return row_dicts
