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

big_count = None
big_emailer = None

for email, count in counts.items():
    if big_count is None or count > big_count:
        big_count = count
        big_emailer = email

print(big_emailer, big_count)
