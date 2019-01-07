import csv
from newsstream import titles, bodies  

headlines = titles 
summaries = bodies

db = csv.reader(open('scored.csv', 'rt'), delimiter=',')


def score(text, db):
    sentence = text.split(' ')
    scores = []

    for row in db:
        for word in sentence:
            if word == row[0]:
                scores.append(int(row[3]))

    return sum(scores)
