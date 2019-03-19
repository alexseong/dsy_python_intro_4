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
        domain = words[1].split('@')[1]
        counts[domain] = counts.get(domain, 0) + 1

print(counts)

big_count = None
big_domain = None

for domain, count in counts.items():
    if big_count is None or count > big_count:
        big_count = count
        big_domain = domain

print(big_domain, big_count)
