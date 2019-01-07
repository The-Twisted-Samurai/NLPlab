from textcleaner import stopwords
import csv

def remove_duplicates(filepath):
    rows = csv.reader(open(filepath, 'rt'))
    new = []

    for row in rows:
        if row not in new:
            new.append(row)

    writer = csv.writer(open(filepath, 'wt'))
    writer.writerows(new)

def clean_db(path):
    csv_reader = csv.reader(open(path, mode='rt'), delimiter=',')
    n = []
    for row in csv_reader:
        if row[0] not in stopwords:
            n.append(row)
    csv.writer(open(path, 'wt')).writerows(n)
    