fname = input('Enter file: ')

try:
    fhand = open(fname)

    list = list()

    for line in fhand:
        words = line.rstrip().split()
        for word in words:
            if word not in list:
                list.append(word)

    list.sort()
    print(list)

except:
    print('Error, opening file')
    exit()