
def dump(data, file):
    header = sorted(set(row for row in data for row in row.keys()))
    rows = [tuple(row.get(key,'') for key in header) for row in data]
    data = [header] + rows
    values = [','.join(f'"{x}"' for x in row) for row in data]
    result = '\n'.join(values) + '\n'
    with open(file, mode='wt') as file:
        file.write(result)
