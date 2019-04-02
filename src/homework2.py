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

    print(dic)

except:
    print('Error, opening file')
    exit()
