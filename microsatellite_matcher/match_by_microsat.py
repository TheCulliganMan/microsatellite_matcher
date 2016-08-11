#!/usr/bin/env python
def match_by_microsat(processed_row_dicts, markers, individual_key="Lab ID"):
    match_set = set()
    for indiv_1 in processed_row_dicts:
        for indiv_2 in processed_row_dicts:

            if indiv_1[individual_key] == indiv_2[individual_key]:
                continue
            full_count = 0

            for marker in markers:
                if marker in indiv_1 and marker in indiv_2:
                    indiv_1_marker = indiv_1[marker]
                    indiv_2_marker = indiv_2[marker]
                    used_pos_1 = []
                    used_pos_2 = []
                    count = 0
                    for num_1, marker_1 in enumerate(indiv_1_marker):
                        for num_2, marker_2 in enumerate(indiv_2_marker):
                            if (num_2 in used_pos_2) or (num_1 in used_pos_1):
                                continue

                            if (marker_1 == marker_2) \
                                    or (-1 in (marker_1, marker_2)):
                                used_pos_1.append(num_1)
                                used_pos_2.append(num_2)
                                count += 1

                    if count >= 2:
                        full_count += 1

            if full_count == indiv_1["marker_count"]:
                if (((indiv_1[individual_key], indiv_2[individual_key])
                     not in match_set)
                        and (indiv_2[individual_key], indiv_1[individual_key])
                        not in match_set):
                    match_set.add(
                        (indiv_1[individual_key], indiv_2[individual_key]))
                    print("MATCH {} {}".format(
                        indiv_1[individual_key], indiv_2[individual_key]))
