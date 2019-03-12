# Lists

### A list is a sequence
 A list is a sequence of values. In a string, the values are characters; in a list, they can be any type. The values in list are called elements or sometimes items.

### Lists are mutable
The flow of while statement


### Infinite loops

    n = 10
    while True:
        print(n, end='')
        n = n - 1
    print('Done!')

    while True:
        line = input('> ')
        if line == 'done':
            break
        print(line)
    print('Done!')

This way of writing while loops is common because you can check the condition anywhere in the loop (not just at the top) and you can express the stop condition affirmatively ("stop when this happens") rather than negatively ("keep going until that happens.").

### Finishing iterations with continue

    while True:
        line = input('> ')
        if line[0] == '#':
            continue
        if line == 'done':
            break
        print(line)
    print('Done!')

### Define loops using for

The <b>for</b> loop is looping through a known set of items so it runs through as many iterations as there are items in the set

### Loop patterns

#### Continuing and summing loops
    len()
    sum()

#### Maximum and minimum loops

    def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest


## [Exercises](./exercises_loop.md)

## [Glossary](./glossary_loop.md)

# Strings

### A string is a sequence
The index is an offset from the beginning of the string, and the offset of the first letter is zero.<br>
The value of the index has to be an integer
    
### Getting the length of a string using len
    len()

To get the last letter

    print(fruit[len(fruit) - 1])
    print(fruit[-1])

Negative indices count backward from the end of the string

### Traversal through a string with a loop
while loop and for loop

### String slices
If the first index is greater than or equal to the second the result is an empty string, represented by two quotation marks:

### Strings are immutable
You can't change an existing string. The best you can do is create a new string that is a variation on the original:

    >>> greeting = 'Hello, world!'
    >>> new_greeting = 'J' + greeting[1:]

### Looping and counting

### The in operator

### String comparison

### String methods
Strigs are Python objects which cointain both data and methods.<br>
dir() for available methods<br>

    >>> stuff = 'Hello world'
    >>> type(stuff)
    >>> dir(stuff)
    >>> help(stuff.capitalize)

We call a method by appending the method name to the variable name using the period as a delimeter. A method call is called an invocation.

    >>> word = 'banana '
    >>> new_word = word.upper()
    >>> index = word.find('a')
    >>> word.strip()
    >>> word.startwith('ba')
    >>> 

### Parcing strings

### Format operator
When the first operand is a string, % is the format operator.<br>
The first operand is the format string, which contains one or more format sequences that specify how the second operand is formatted.<br>

    %d
    %g
    %s


## [Exercises](./exercises_string.md)

## [Glossary](./glossary_string.md)

# FILES

## Opening files
If the open is successful, the operating system returns us a file handle.

## Text files and lines
    data/mbox.txt
    data/mbox_short.txt

## Reading files
    fhand = open('filename')
    for line in fhand:
        # do something
    
    str = fhand.read()

## Searching through a file
    str_obj.rstrip()
    str_obj.startwith('')

## Letting the user choose the file name
    fname = input('Enter the file name: ')
    fhandle = open(fname)

## Using try, except, and open
more Pythonic way

## Writing files
    fout = open('output.txt', 'w')
    line1 = "This is the first line.\n"
    fout.write(line1)
    fout.close()

    

## [Exercises](./exercises_file.md)

## [Glossary](./glossary_file.md)

# [Week 5 Assignments](assignment.md)