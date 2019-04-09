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
        dic[words[1]] = dic.get(words[1],0) + 1
list = list()
for v,k in dic.items():
    newtup = (v,k)
    list.append(newtup)

list = sorted(list, reverse=True)

print(list,[0][1],list[0][0])
