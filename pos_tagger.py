import spacy
import csv
import sys

# For pretty printing of tokenisation
def print_table(doc):
    header = '| {:8} | {:8} | {:8} | {:8} | {:10} | {:8} | {:8} | {:8} |'.format("Text", "Lemma", "PoS", "Tag", "Dependency", "Shape", "Alpha", "Stop")
    separator = '-' * len(header)

    print(header)
    print(separator)
    
    for token in doc:
        print('| {:8} | {:8} | {:8} | {:8} | {:10} | {:8} | {:8} | {:8} |'.format(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop))

# Write tagged.csv to the current directory
def write_csv(doc):
    with open('tagged.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for token in doc:
            writer.writerow([token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop])


# Load English as the language and get the text to be parsed
nlp = spacy.load('en_core_web_sm')
text = sys.argv[1]

doc = nlp(u'{}'.format(text))
#doc = nlp(u"Kotak Mahindra stocks fall due to bad quarter")

write_csv(doc)
#print_table(doc)
