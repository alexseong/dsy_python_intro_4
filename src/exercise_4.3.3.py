import string

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
    fhand = open(fname)
except:
    print('File does not exist.')
    exit()

chr_counts = dict()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()

    for word in words:
        for chr in list(word):
            if chr.isalpha():
                chr_counts[chr] = chr_counts.get(chr, 0) + 1

chr_list = list()

for chr, count in chr_counts.items():
    chr_list.append((count, chr))

chr_list.sort(reverse=True)

for char_tuple in chr_list:
    print(char_tuple[1], char_tuple[0])
