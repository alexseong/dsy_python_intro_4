fname = input("Enter file name: ")
if len(fname) < 1 : fname = "words.txt"

fh = open(fname)
word_dict = {}

for line in fh:
    words = line.rstrip().split()
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1

print(word_dict)
