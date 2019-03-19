fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From '):
        words = line.rstrip().split()
        print(words[2])
