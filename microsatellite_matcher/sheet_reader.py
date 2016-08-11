#/usr/bin/env python
import xlrd


def go_by_row(sheet):

    keys = [sheet.cell(
        0, col_index).value for col_index in xrange(sheet.ncols)]
    row_dicts = []
    for row_index in range(1, sheet.nrows):
        row_dict = {}
        for col_index in xrange(sheet.ncols):
            if keys[col_index]:
                val = sheet.cell(row_index, col_index).value
                if val:
                    if "@" in keys[col_index]:
                        if ("*" not in str(val)):
                            row_dict[keys[col_index]] = int(val)
                        else:
                            row_dict[keys[col_index]] = -1
                    else:
                        row_dict[keys[col_index]] = val
        row_dicts.append(row_dict)
    return keys, row_dicts


def get_workbook_dicts(file_name):
    xl_workbook = xlrd.open_workbook(file_name)
    sheet_names = xl_workbook.sheet_names()
    xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
    keys, row_dicts = go_by_row(xl_sheet)
    return keys, row_dicts
