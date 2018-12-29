from spacy.pipeline import Tagger
from spacy.lang.en import English

def print_table(doc):
    header = '{:8} | {:8} | {:8} | {:8} | {:10} | {:8} | {:8} | {:8} |'.format("Text", "Lemma", "PoS", "Tag", "Dependency", "Shape", "Alpha", "Stop")
    seperator = '-' * len(header)

    print(header)
    print(seperator)
    
    for token in doc:
        print('{:8} | {:8} | {:8} | {:8} | {:10} | {:8} | {:8} | {:8} |'.format(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop))


nlp = English()

tagger = Tagger(nlp.vocab)

doc = nlp.make_doc(u"Kotak Mahindra stocks fall due to bad quarter.")

print_table(doc)

#for token in doc:
#    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#          token.shape_, token.is_alpha, token.is_stop)
#    print_table(token)
