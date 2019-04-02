fname = input('Enter File Name: ')
if len(fname) < 1 : fname = "words.txt"

fh = open(fname)
word_dict = {}
for line in fh:
    words = line.rstrip().split()
    for wors in words:
        word_dict[word] = word_dict.get(word, 0) + 1

print(word_dict)
