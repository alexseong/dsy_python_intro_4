<b><Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.</b>

<b>Exercise 2: Figure out which line of the below program is still not properly guarded. See if you can construct a text file which causes the program to fail and then modify the program so that the line is properly guarded and test it to make sure it handles your new text file.</b>

    fhand = open('mbox-short.txt')
    count = 0
    for line in fhand:
        words = line.split()
        # print 'Debug:', words
        if len(words) == 0: 
            continue
        if words[0] != 'From': 
            continue
        print(words[2])

<b>Exercise 3: Rewrite the guardian code in the above example without two if statements. Instead, use a compound logical expression using the and logical operator with a single if statement.</b>

<b>Exercise 4: Write a program to open the file elite.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list. When the program completes, sort and print the resulting words in alphabetical order.</b>

    Enter file: elite.txt
    ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

<b>Exercise 5: Write a program to read through the mail box data and when you find line that starts with "From", you will split the line into words using the split function. We are interested in who sent the message, which is the second word on the From line.</b>

    From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

You will parse the From line and print out the second word for each From line, then you will also count the number of From (not From:) lines and print out a count at the end. This is a good sample output with a few lines removed:

    python exercise4.1.5.py
    Enter a file name: mbox-short.txt

    stephen.marquard@uct.ac.za
    louis@media.berkeley.edu
    zqian@umich.edu

    [...some output removed...]

    ray@media.berkeley.edu
    cwen@iupui.edu
    cwen@iupui.edu
    cwen@iupui.edu
    There were 27 lines in the file with From as the first word


<b>Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters "done". Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.</b>

    Enter a number: 6
    Enter a number: 2
    Enter a number: 9
    Enter a number: 3
    Enter a number: 5
    Enter a number: done
    Maximum: 9.0
    Minimum: 2.0




