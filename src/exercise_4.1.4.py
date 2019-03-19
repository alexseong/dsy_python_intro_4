fname = input("Enter file name: ")
if len(fname) < 1 : fname = "elite.txt"

try:
    fh = open(fname)

    lst = []

    for line in fh:
        words = line.rstrip().split()
        for word in words:
            if word not in lst:
                lst.append(word)

    lst.sort()
    print(lst)
except:
    print("File doesn't exist")
    exit(-1)
