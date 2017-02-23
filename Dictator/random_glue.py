import sys, string
from textblob import TextBlob
import codecs
import random

text = sys.stdin.read()
text = text.decode('ascii', errors='ignore')
text = text.lower()

blob = TextBlob(text)

noun_phrases = blob.noun_phrases

verbs = list()

instruction_num = 10

for word,tag in blob.tags:
    if tag == 'VB':
        verbs.append(word.lemmatize())

sample_phrases = random.sample(noun_phrases,instruction_num)
sample_verbs = random.sample(verbs,instruction_num)
for i in range(0,instruction_num):
    print "I want to " + sample_verbs[i]+' '+sample_phrases[i]
