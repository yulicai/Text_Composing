import sys,string
from textblob import TextBlob
from collections import Counter
import codecs
import random


whole_line = ""
verbs = []
nouns = []
adjectives = []
text = sys.stdin.read()
text = text.lower()
text = text.translate(string.maketrans("",""), string.punctuation)
# text = sys.stdin.read().decode('ascii', "ignore")
blob = TextBlob(text)
tags = blob.tags
for word,tag in blob.tags:
    if ("VB" in tag):
        verbs.append(word)
    if ("NN" in tag):
        nouns.append(word)
    if ("JJ" in tag):
        adjectives.append(word)

verb_counter = Counter(verbs)
noun_counter = Counter(nouns)
adjective_counter = Counter(adjectives)
# print counter.keys()
# all_words = counter.keys()
# print "<<<<<<<<<<<<<< ALL THE NOUN WORDS"
# for word in all_words:
#     print word


# print "<<<<<<<<<<<<<< FOLLOWING ARE TOP 40"
verb_most_common = verb_counter.most_common(40)
noun_most_common = noun_counter.most_common(40)
adjective_most_common = adjective_counter.most_common(40)

verb_random_ai = random.sample(verb_most_common,10)
noun_random_ai = random.sample(noun_most_common,10)
adjective_random_ai = random.sample(adjective_most_common,10)

verb_random_cn = random.sample(verb_most_common,10)
noun_random_cn = random.sample(noun_most_common,10)
adjective_random_cn = random.sample(adjective_most_common,10)

ai_sentences = []
for index in range(0,10):
    verb_str = str(verb_random_ai[index][0].lemma)
    noun_str = str(noun_random_ai[index][0])
    adjective_str = str(adjective_random_ai[index][0])
    ai_sentences.append("Aiweiwei claims "+ verb_str + "ing " + adjective_str+ " "+noun_str)

cn_sentences = []
for index in range(0,10):
    verb_str = str(verb_random_cn[index][0].lemma)
    noun_str = str(noun_random_cn[index][0])
    adjective_str = str(adjective_random_cn[index][0])
    cn_sentences.append("Chinese government says "+ verb_str + "ing " + adjective_str+ " "+noun_str)

for index in range(0,10):
    print ai_sentences[index]+'. '
    print cn_sentences[index]+'.'
    print ' '
# print ai_sentences
# print cn_sentences
