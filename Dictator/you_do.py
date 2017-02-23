import sys, string
from textblob import TextBlob
import codecs
import random

text = sys.stdin.read()
text = text.decode('ascii', errors='ignore')
text = text.lower()

blob = TextBlob(text)


verbs = list()

instruction_num = 10

for word,tag in blob.tags:
    if tag == 'VB':
        verbs.append(word.lemmatize())

sample_verbs = random.sample(verbs,instruction_num)
for i in range(0,instruction_num):
    print "You " + sample_verbs[i]+'.'
