# Lists

### A list is a sequence
 A list is a sequence of values. In a string, the values are characters; in a list, they can be any type. The values in list are called elements or sometimes items.

### Lists are mutable
The flow of while statement

    >>> numbers = [17, 123]
    >>> numbers[1] = 5
    >>> print(numbers)
* Any integer expression can be used as an index.
* If you try to read or write an element that does not exist, you get an IndexError.
* If an index has a negative value, it counts backward from the end of the list.

### Traversing a list

    for cheese in cheeses:
    print(cheese)

    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2

### List operations
The + operator concatenates lists<br>
Similarly, the * operator repeats a list a given number of times

### List slices
A slice operator on the left side of an assignment can update multiple elements

### List methods

    >>> t = ['a', 'b', 'c']
    >>> t.append('d')
    >>> print(t)
    ['a', 'b', 'c', 'd']

    >>> t1 = ['a', 'b', 'c']
    >>> t2 = ['d', 'e']
    >>> t1.extend(t2)
    >>> print(t1)
    ['a', 'b', 'c', 'd', 'e']

    >>> t = ['d', 'c', 'e', 'b', 'a']
    >>> t.sort()
    >>> print(t)
    ['a', 'b', 'c', 'd', 'e']

### Deleting elements

    >>> t = ['a', 'b', 'c']
    >>> x = t.pop(1)
    >>> print(t)
    ['a', 'c']
    >>> print(x)
    b

    >>> t = ['a', 'b', 'c']
    >>> del t[1]
    >>> print(t)
    ['a', 'c']

    >>> t = ['a', 'b', 'c']
    >>> t.remove('b')
    >>> print(t)
    ['a', 'c']


### Lists and functions

    numlist = list()
    while (True):
        inp = input('Enter a number: ')
        if inp == 'done': break
        value = float(inp)
        numlist.append(value)

    average = sum(numlist) / len(numlist)
    print('Average:', average)

### Lists and string

    >>> s = 'spam'
    >>> t = list(s)
    >>> print(t)
    ['s', 'p', 'a', 'm']

The list function breaks a string into individual letters. If you want to break a string into words, you can use the split method

    >>> s = 'spam-spam-spam'
    >>> delimiter = '-'
    >>> s.split(delimiter)
    ['spam', 'spam', 'spam']

    >>> t = ['pining', 'for', 'the', 'fjords']
    >>> delimiter = ' '
    >>> delimiter.join(t)
    'pining for the fjords'

### Parsing lines

    fhand = open('mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if not line.startswith('From '): continue
        words = line.split()
        print(words[2])

### Objects ans values

    >>> a = 'banana'
    >>> b = 'banana'
    >>> a is b
    True

    >>> a = [1, 2, 3]
    >>> b = [1, 2, 3]
    >>> a is b
    False

### Aliasing

An object with more than one reference has more than one name, so we say that the object is aliased. <br>If the aliased object is mutable, changes made with one alias affect the other:

### List arguments

When you pass a list to a function, the function gets a reference to the list. If the function modifies a list parameter, the caller sees the change. For example, delete_head removes the first element from a list:


## [Exercises](./exercises_list.md)

## [Glossary](./glossary_list.md)


# Dictionaries

In a dictionary, the indices can be (almost) any type.<br>
Each key maps to a value. The association of a key and a value is called a key-value pair or sometimes an item.

    >>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
    >>> print(eng2sp)
    {'one': 'uno', 'three': 'tres', 'two': 'dos'}

    >>> 'one' in eng2sp
    True
    >>> 'uno' in eng2sp
    False

    >>> vals = list(eng2sp.values())
    >>> 'uno' in vals
    True

The in operator uses different algorithms for lists and dictionaries. For lists, it uses a linear search algorithm. As the list gets longer, the search time gets longer in direct proportion to the length of the list. For dictionaries, Python uses an algorithm called a hash table that has a remarkable property: the in operator takes about the same amount of time no matter how many items there are in a dictionary. 

### Dictionary as a set of counters

    word = 'brontosaurus'
    d = dict()
    for c in word:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    print(d)

    word = 'brontosaurus'
    d = dict()
    for c in word:
        d[c] = d.get(c,0) + 1
    print(d)

### Dictionaries and files
    fname = input('Enter the file name: ')
    
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        exit()
    
    counts = dict()
    
    for line in fhand:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
    
    print(counts)

### Looping and dictionaries

    counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
    lst = list(counts.keys())
    print(lst)
    lst.sort()
    for key in lst:
        print(key, counts[key])

### Advanced text parsing

    import string
    
    fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        exit()
    
    counts = dict()
    for line in fhand:
        line = line.rstrip()
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
    
    print(counts)

## [Exercises](./exercises_dict.md)

## [Glossary](./glossary_dict.md)

# [Week 8 Assignments](assignment.md)