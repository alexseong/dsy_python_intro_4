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
        words = line.rstrip().split(':')
        hour = words[0][-2:]
        counts[hour] = counts.get(hour, 0) + 1

hour_list = list()

for hour in sorted(counts):
    print(hour, counts[hour])
