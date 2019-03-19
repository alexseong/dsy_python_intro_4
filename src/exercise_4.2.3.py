fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox.txt"

try:
    fhand = open(fname)
except:
    print('File does not exist.')
    exit()

counts = dict()

for line in fhand:
    if line.startswith('From: '):
        words = line.rstrip().split()
        counts[words[1]] = counts.get(words[1], 0) + 1

print(counts)
