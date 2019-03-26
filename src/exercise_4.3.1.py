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

domain_list = list()

for domain, count in counts.items():
    domain_list.append((count, domain))

domain_list.sort(reverse=True)
print(domain_list[0][1], domain_list[0][0])
