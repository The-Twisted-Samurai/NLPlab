# Notebook to run experiments and visualisations 
from newsstream import titles, bodies  
import csv 
headlines = titles 
summaries = bodies
# pos_list(headlines)
import spacy
from syntax import score_syntax, score
import matplotlib.pyplot as plt 


scores = score_syntax(headlines)
x = list(range(len(scores)))
plt.scatter(x,scores)
if input("display articles? [Y/n]:") == "":
    for headline in headlines:
        print("Article: ",headline)
        print("risk score(syntax):",score(headline))
        print("-")
    else: 
        pass
avg = sum(scores)/len(scores)
print("Average risk of set (semantic):", int(avg))

def semantic_test(headline):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(headline)
    sent = headline.split(" ")
    dependencies = []
    pos = []
    docM_base = [sent, dependencies, pos]
    for token in doc:
        dependencies.append(token.dep_)
        pos.append(token.pos_)

    return docM_base

test = semantic_test(headlines[2])
for n in test:
    print(n)