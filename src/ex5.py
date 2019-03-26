fname = input('Enter file: ')

count = 0
try:
    fhand = open(fname)

    for line in fhand:
        if line.startswith('From'):
            words = line.strip().split()
            print(words[1])
            count = count +1

    print('There were',count,'lines in the file with From as the first word')

except:
    print('Error, opening file')
    exit()
