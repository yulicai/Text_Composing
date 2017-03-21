# POETIC FORM INSTRUCTIONS
# For the content
# Definition of art from different artist
###########
# For the form
# First thing to be determined is the length of the triangle N, which equals to the length of the first line
# It has N lines, the last line contains only one word
# The first word of each line starts from a phone of AA1 R (referencing art)

import pronouncing as pr
from textblob import TextBlob
import sys
import random

## PART ONE >> Generate a pool for the first word of each line

#search for the pronouncing or the first two syllabus in the word art
#print ar gives us result as "AA1 R" which has 5 characters
ar = pr.phones_for_word('art')[0][:5]
ar_wordlist=list()
ar_wordlist = pr.search('^'+ar)
ar_short = list()
#select the word less then 9 characters into a new list ar_short
for word in ar_wordlist:
    if len(word)<9:
        ar_short.append(word)

#recombine the words in the list together to a string to feed into textblob
ar_short_text = " ".join(ar_short)
blob = TextBlob(ar_short_text)
tags = blob.tags

#create a list to hold the nouns within the list ar_short
ar_nouns = list()
for word,tag in blob.tags:
    if 'NN' in tag:
        ar_nouns.append(word)

## PART ONE END <<

#system feed the program a source text
source_text = sys.stdin.readlines()
#give is a triangle/poem length number(int)
side_length = sys.argv[1]
# create a dictionary to sort lines by length, length is the key
by_length = {}

for line in source_text:
    words = line.split()
    if len(words) not in by_length:
        by_length[len(words)]=[]
    by_length[len(words)].append(line)

sorted_length = sorted(by_length)
#poem_dict, key is the counter number, value is the according line from the original text
poem_dict={}
counter = int(side_length)
while (counter>0):
    #if there are multiple lines for the same length, randomly choose one line
    random_index = random.randrange(len(by_length[sorted_length[counter-1]]))
    poem_dict[counter]=(by_length[sorted_length[counter-1]][random_index])
    counter = counter-1

final_poem = []
indexes = sorted(poem_dict,reverse=True)
for num in indexes:
    line = poem_dict[num]
    words = line.split()
    #using the art substitude from the ar_nouns made at the first part
    words[0] = random.choice(ar_nouns)
    new_line =" ".join(words[:num])
    final_poem.append(new_line)

for l in final_poem:
    print l
print ">>>>>>>>>>>>>>\n\n"


# counter = int(side_length)
# while (counter > 0) :
#     if counter in by_length.keys():
#         final_poem.append(by_length[counter][0])
#     else:
#         min_abs = 100
#         # to record the diff and its original key number in by_length
#         track_key = 0
#         for key in by_length:
#             diff = abs(key-counter)
#             if diff<min_abs:
#                 min_abs = diff
#                 track_key = key
#         final_poem.append(by_length[track_key][0])
#     counter = counter-1
