
def import_col_file():
    with open('base_col.csv', 'r') as file:
        data = file.readlines()
    return data


def import_row_file():
    with open('base_row.csv', 'r') as file:
        data = file.read()
    return data
