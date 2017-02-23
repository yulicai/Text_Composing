import sys

word_list=[]
minLen = 0
# for n in sys.argv[1:]:
    # print n
file1 = open(sys.argv[1])
file1_lines = file1.readlines()

file2 = open(sys.argv[2])
file2_lines = file2.readlines()


if(len(file1_lines)<len(file2_lines)):
    minLen = len(file1_lines)
else:
    minLen = len(file2_lines)
i = 0
while(i < minLen):
    word_list.append(file1_lines[i] +", "+file2_lines[i])
    i += 1

for item in word_list:
    item = item.replace('\n','')
    print item
