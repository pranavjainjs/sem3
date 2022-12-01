# Assignment 4

*Name* : Pranav Jain \
*Roll no* : 210101078 \
*OS* : Ubuntu 22.04.1 LTS

Submitted to : Dr. Pinaki Mitra / Ms. Sumita Majhi
on Nov 15, 2022.

The zip file contains submission for Programming-Assignment-2.
It contains following files  
 - q1.py 
 - q2a.tex
 - q2b.tex
 - README.md

## Task 1
It requires the use of python programming language.

### To run the program
- Enter "python q1.py" OR "python3 q1.py" in terminal

### Parameters input in command line
- Value of Money (amount)

Note that input can be arbitrarily large.

### Explanation
- My approach to the problem is based on dynamic programming. 
- To compute totalCoins(n), we calculate the number of 50 unit coins and remaining coins separately and add them.
- Number of 50 unit coins = [amount//50]
- Number of other unit coins = minimum value among {totalCoins(n-1), totalCoins(n-5), totalCoins(n-10), totalCoins(n-20), totalCoins(n-25)} + 1 as {1, 5, 10, 20, 25} are the denominations we are available with.

### Test Case
Enter the amount: 
    47

Output -

minimum number of coins needed -  4
25 unit coins - 1
20 unit coins - 1
1 unit coins - 2

## Task 2
Writing LaTeX script

### To compile the program 
- Enter : "pdflatex q2a.tex" and "pdflatex q2b.tex".
- Find "q2a.pdf" or "q2b.pdf" files among the output files.
- Alternatively, you can use Papeeria or Overleaf to compile and view the resulting pdf file.

### Caution
- Please compile "q2a.tex" again in case you see ?? in place of hyperlinks

### Packages used
- amsmath : to display math symbols
- hyperref : to create internal links