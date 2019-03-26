def chop(list):
    list.remove(list[0])
    endNum = len(list) - 1
    list.remove(list[endNum])
    print(list)

list = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    list.append(value)

chop(list)
