fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
    fhand = open(fname)
except:
    print('File does not exist.')
    exit()

counts = dict()

for line in fhand:
    if line.startswith('From '):
        words = line.rstrip().split()
        counts[words[2]] = counts.get(words[2], 0) + 1

print(counts)
