This is little more that a data science excercise that attempts to predict winning numbers of the California SuperLotto.  It does this based on all sorts of frequency and difference-between-occurence tests.  So far, it has failed to produce numbers that are much better than random guesses.

The SuperLotto game has gone through almost 2,000 draws during it's existence.  This program works by cumulating draws from the first to (number_of_draws - testlen), where testlen is a program parameter.  After (number_of_draws - testlen) number of draws, it starts re-calculating the most probable numbers for each draw, and calculating how many numbers it got right and keeps a running total for that #testlen number of draws.  My best run so far paid a $22 return on $100 in tickets, a 78% loss.

lotto.py - main executable that analyzes the lottery numbers

lottosorted.txt - formatted lottery numbers from the SuperLotto Plus on the California Lottery Website

sortrawcp.ph - Stands for Sort Raw Copy Paste.  Go to the view all numbers section of the Superlotto Plus winning numbers section, copy and paste the numbers that you need to update lottosorted.txt, save them in a file called "copypasteupdate.txt".  Execute sortrawcp.py without any arguments, it will create "lottoupdate.txt".  Copy and paste this into lottosorted.txt, and it will update your lottery numbers file.
