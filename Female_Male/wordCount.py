import sys,string
from collections import Counter

whole_line = ""
word_list = []

for line in sys.stdin:
    line = line.split('\n')
    whole_line += line[0]+" "

whole_line = whole_line.lower()
#remove all the punctuations
whole_line = whole_line.translate(string.maketrans("",""), string.punctuation)
word_list = whole_line.split()

counter = Counter(word_list)
most_common = counter.most_common(10)
for item in most_common:
    print item[0]
