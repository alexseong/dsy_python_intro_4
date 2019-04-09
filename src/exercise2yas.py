name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

try:
    fhand = open(name)

except:
    print('Error, opening file')
    exit()

counts = dict()

for line in fhand:
    if line .startswith('From '):
        words = line.rstrip().split(':')
        hour = words[0][-2:]
        counts[hour] = counts.get(hour,0) + 1
hour_list = list()
for hour in sorted(counts):
    print(hour, counts[hour])
