from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import spacy
from spacy import displacy

app = FastAPI()

origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    # "http://localhost:3000",
    "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# [tokenization, pos, stemming, lemmatization]


nlp = spacy.load('en_core_web_sm')
# nlp = spacy.load('en_core_web_lg')


"""
doc = nlp(u'Tesla is looking at buying U.S. startups for $6 million')
for token in doc:
    print(token.text, token.pos_, token.dep_ )
    .text, .lemma_, .pos_, .tag_, .shape_, .is_alpha, .is_stop
for sentence in doc.sents:
    print(sentence)
    
doc = nlp(mystring)
len(doc)

for token in doc:
    print(token.text, end=' | ')

for entity in doc.ents:
    print(entity)
    print(entity.label_)
    print(str(spacy.explain(entity.label_)))
    print('\n')
for chunk in doc.noun_chunks:
    print(chunk)

from spacy import displacy
displacy.render(doc, style='dep', jupyter=True, options={'distance':50})

displacy.render(doc, style='ent', jupyter=True)

displacy.serve(doc, style='dep')

for token in doc:
    print(token.text, '\t', token.pos_, '\t', token.lemma, '\t', token.lemma_ )

def show_lemmas(text):
    for token in text:
        print(f"{token.text:{12}} {token.pos_:{6}} {token.lemma:<{22}} {token.lemma_}")

tasks:
1, check how to implement in fastapi/flask
2, check how to return more than 1 result
"""


#
# def show_pos(text):
#     doc = nlp(text)
#     for token in doc:
#         result = f"{token.pos_}"
#         return result


@app.get('/')
async def root():
    return "Welcome"


@app.get('/pos/{text}')
async def receive(text: str):
    doc = nlp(text)
    pos_list = [(word.text, word.pos_, word.dep_ ) for word in doc]
    return pos_list
