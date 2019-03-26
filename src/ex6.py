
list = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    list.append(value)


print(max(list))
print(min(list))
