import markov
import sys
import random

time_pool = ["10:24 PM","11:30 PM", "2:35 AM", "7:01 PM ", "11:50 PM ", "2:03 PM", "2:00 AM" ]
lines = list()
for line in open("drunk_text.txt"):
    line = line.strip()
    if(len(line)>0):
        lines.append(line)

# using markov
model = markov.build_model(lines,4)
generate_result = markov.char_level_generate(lines,4, count = 10)
# generate_result = markov.word_level_generate(lines,2, count = 10)
print random.choice(time_pool)+"\n "
for m in generate_result:
    print"Dude: \n" + "     "+ m

print "\n" + ">>>>>>>>>>>>>>>"+"\n" + "\n"+ "\n"






# Saved for later
# Triallllll
# for verizon look
model_result = markov.generate(model,5)
new_matrix = dict()
col_num = len(model_result)
for i in range(col_num):
    new_matrix[i] = list()
    for m in model_result:
        words = m.strip()
        if(i<m):
            new_matrix[i].append(words[i])
# print new_matrix.values()
