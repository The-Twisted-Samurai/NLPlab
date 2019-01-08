import csv
def score(text):
    db = csv.reader(open("scored.csv", mode='rt'), delimiter=',')
    sentence = text.split(' ')
    scores = []
    for row in db:
        for word in sentence:
            if word == row[0]:
                scores.append(int(row[3]))
    print("")
    return sum(scores)

def score_syntax(docs):
    scores = []
    for k in docs:
        scores.append(score(k))
    return scores

