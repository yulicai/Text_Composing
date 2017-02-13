import sys,string
from textblob import TextBlob
from collections import Counter
import codecs

whole_line = ""
word_list = []
text = sys.stdin.read()
text = text.lower()
text = text.translate(string.maketrans("",""), string.punctuation)
# text = sys.stdin.read().decode('ascii', errors="replace")
blob = TextBlob(text)
tags = blob.tags
for word,tag in blob.tags:
    if ("NN" in tag):
        word_list.append(word)
        # print word

counter = Counter(word_list)
most_common = counter.most_common(10)
for item in most_common:
    print item[0]

# for item in most_common:
    # print item[0]
