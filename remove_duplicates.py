import csv

def remove_duplicates(filepath):
    rows = csv.reader(open(filepath, 'rt'))
    new = []

    for row in rows:
        if row not in new:
            new.append(row)

    writer = csv.writer(open(filepath, 'wt'))
    writer.writerows(new)

