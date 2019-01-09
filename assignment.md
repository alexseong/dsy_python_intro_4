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
1. Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 for input data.
Using atom text editor, open ./src/assignment_3.1.py and write your program.
<br>Compare your output with 'Desired Output'

    Desired Output:<br> 

        Invalid input
        Maximum is 10
        Minimum is 2

2. Write code using find() and string slicing to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

Using atom text editor, open ./src/assignment_3.2.py and write your program.
<br>Compare your output with 'Desired Output'
 

    Desired Output: 
            0.8475


3. Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

    X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at [./data/pymbox-short.txt](https://github.com/alexseong/dsy_python_intro_3/blob/master/data/mbox-short.txt) when you are testing below enter mbox-short.txt as the file name.

Using atom text editor, open ./src/assignment_3.3.py and write your program.
<br>Compare your output with 'Desired Output'

    Desired Output: 
            Average spam confidence: 0.750718518519

