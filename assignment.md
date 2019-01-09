# Python Assignment


## Part 0: Fork and clone the repo

You should make your own copy of the repository so that you can edit it and at the end submit a pull request.

1. Create a fork of this repo by clicking on the **Fork** link in the upper right.
2. Checkout your personal copy of the repo: `git clone https://github.com/<username>/python-intro1`

### How to submit?
1. `git add filename` (or `git add .`) for all the files you want to add.
2. `git commit -m "Message describing what you did"`
3. `git push origin master`
4. Now if you go to your personal copy on github, your changes should be there: `https://github.com/<username>/python-intro1`
5. From there, click on **Pull Requests** and then **New pull request**.

Ideally, you should regularly run steps 1-3. This will save your work as you go. And if you ever goof things up, you will have all the history, you can revert any file to how it was at any previous commit!

## Exercise 
1.1 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at [./data/romeo.txt](https://github.com/alexseong/dsy_python_intro_4/blob/master/data/romeo.txt)
Using atom text editor, open ./src/assignment_4.1.1.py and write your program.
<br>Compare your output with 'Desired Output'

    Desired Output:<br> 

        ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

1.2 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:

    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at [./data/mbox-short.txt](https://github.com/alexseong/dsy_python_intro_4/blob/master/data/mbox-short.txt)
Using atom text editor, open ./src/assignment_4.1.2.py and write your program.
<br>Compare your output with 'Desired Output'

    Desired Output:<br> 

        stephen.marquard@uct.ac.za
        louis@media.berkeley.edu
        zqian@umich.edu
        rjlowe@iupui.edu
        zqian@umich.edu
        rjlowe@iupui.edu
        cwen@iupui.edu
        cwen@iupui.edu
        gsilver@umich.edu
        gsilver@umich.edu
        zqian@umich.edu
        gsilver@umich.edu
        wagnermr@iupui.edu
        zqian@umich.edu
        antranig@caret.cam.ac.uk
        gopal.ramasammycook@gmail.com
        david.horwitz@uct.ac.za
        david.horwitz@uct.ac.za
        david.horwitz@uct.ac.za
        david.horwitz@uct.ac.za
        stephen.marquard@uct.ac.za
        louis@media.berkeley.edu
        louis@media.berkeley.edu
        ray@media.berkeley.edu
        cwen@iupui.edu
        cwen@iupui.edu
        cwen@iupui.edu
        There were 27 lines in the file with From as the first word

2. Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

Using atom text editor, open ./src/assignment_4.2.py and write your program.
<br>Compare your output with 'Desired Output'
 

    Desired Output: 
            cwen@iupui.edu 5


3. Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

Using atom text editor, open ./src/assignment_4.3.py and write your program.
<br>Compare your output with 'Desired Output'

    Desired Output: 
            04 3
            06 1
            07 1
            09 2
            10 3
            11 6
            14 1
            15 2
            16 4
            17 2
            18 1
            19 1

