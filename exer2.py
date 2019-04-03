fhand = input('Enter a file: ')

try:
    fname = open(fhand)
except:
    exit()

dic = dict()

for line in fname:
    if line.startswith('From '):
        line2 = line.rstrip().split(":")
        hour = line2[0][-2:]
        print(hour.append.dic())
