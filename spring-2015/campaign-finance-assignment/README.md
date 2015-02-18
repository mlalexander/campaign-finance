# Campaign finance assignment

Today you'll be receiving your first programming assignment, which will require you to do basic cleanup on some campaign finance data from New York City.

The two files you'll need for the assignment can be found in this directory. You can download them directly to your hard drives or just copy the text/code out into local versions. Just be sure to store them in the same directory on your machines.

You'll see some code already in the clean-donors.py file, which you should leave in place. I've marked the area where you should perform the actual cleaning (though if you want to put it somewhere else, that's fine too). You'll also find further instructions in the comments at the top of that file.

This assignment will be due **Monday, February 23** and should be checked into your Github account (the creation of which is Part 1 of the assignment). You should then e-mail the URL of your Github account to **chase.davis@gmail.com**

As with most problems in data journalism, there isn't one "right" way to approach this. As long as the output is correct, that's all you need to worry about. Hint: This [Python cheat sheet](https://github.com/cjdd3b/advanced-data-journalism/blob/master/spring-2014/lecture-02-10/python-basics.md) might also come in handy.

Parts of assignment
===================

  - Create a Github account and a new open repository to hold this code. You can call it anything you want. Instructions on setting up Git can be found here: https://help.github.com/articles/set-up-git/

  - In the code, perform (almost) the same cleaning operations we did in the exercise last week, except this time on the entire dataset rather than just one row. Those operations are:
    - Set the field containing the first name to all caps
    - Remove &nbsp; characters from the city field
    - Be sure the amount field is typecast to a float
    - Be sure the ZIP field is typecast to a string

  - Add a conditional statement that will print out contributions of more than $5,000

  - Add a separate conditional that will print out contributions from outside New York State