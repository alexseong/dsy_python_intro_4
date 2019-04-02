fname = input('Enter a file name: ')

try:
    fhand = open(fname)

except:
    print('Error, opening file')
    exit()

dic = dict()

for line in fhand:
    if line .startswith('From'):
        words = line.rstrip().split()
        dic[words[2]] = dic.get(words[2],0) + 1

bigcount = none
bigword = none
for word, count in dic.items():
    if bigcount is none or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
