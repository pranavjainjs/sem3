# Assignment 2

*Name* : Pranav Jain \
*Roll no* : 210101078 \
*OS* : Ubuntu 22.04.1 LTS

Submitted to : Dr. Pinaki Mitra / Ms. Sumita Majhi
on Sept 13, 2022.

The zip file contains submission for Programming-Assignment-2.
It contains following sub-directories  
 - Task 1  
 - Task 2

## Task 1

It requires using bash scripting. 

### Assumptions :-
- After the last record, a newline character is required in input.txt file.
- End of Line Sequence is LF.

### Parameters input in command line
- <input> input.txt file containing list of files to be backed up.
- <copy_to> directory where backed up files are stored.

### Explanation
- Go to <copy_to> directory, and check if a <backup> directory already exists.
- If it already exists, delete the directory and backup the updated files. 
- Throw error messages if the number of arguments entered in command line is not equal to 2.
- Else, read each line from the input file, and then copy the file to the destination address.
- Change directory to the <copy_to/backup> directory, and if a backup corresponding to each line in input file exists, print success message.

### Testing the script with
1. No arguments -
Prints "enter parameters"

2. One argument -
Prints "one paramener too few"

3. Three arguments -
Prints "one parameter too many"

4. Any other number of arguments -
Prints "Only 2 parameters are allowed"

5. Two arguments, first is not the name of a file -
Prints "there is no such input file"

6. Two arguments, second one is name of a file rather than directory -
The terminal throws error as the 'cp' command is unable to copy file from a directory to the another, because the destination is not a valid directory name.

7. Name of the file in first argument and the name of the directory in second argument -
The concerned files are successfully backed up to the specified directory.

### Desired Output 
After a successful operation, we get the following output.

`1.txt backed up`\
`2.txt backed up`\
`3.txt backed up`\
`4.txt backed up`\
`all 4 files are successfully duplicated.`\
`the files are -`\
`1.txt.bak 2.txt.bak 3.txt.bak 4.txt.bak`

## Task 2

The question required the use of PERL Programming language. \
Perl is a general-purpose, high level programming language originally developed for text manipulation. \
Perl is an interpreted language, which means that your code can be run as-is, without a compilation stage that creates a non-portable executable program.

### Assumptions :-
- The input.txt file contains a single string, and only one line.
- End of Line Sequence is LF.

### Parameters input in command line
- length (maximum permissible length of string)
- count (max number of times a char can be repeated)

### Description
Run the perl script using `perl file.pl` 

The command line asks you to enter maximum permissible 
length of resultant string. 
Valid values are any number greater than or equal to 1.

Eventually, the command line asks to enter the maximum number of times a char can be repeated in the final string.
Valid values are integers in the range [1, length].

Read the output string.

### Illustration
`perl file.pl` 

`maximum length of string can be` : 30 

`maximum times an alphabet is repeated continuously` : 6 

Generated String -> `ccccckkkkkbbssdaaaabddlllllmss`

### Explanation
string in input.txt file\
`vmnbzsdmnfbsdckjdskdhfdspqworrisahlkdmxcvbm`

random index - char at that index - count of char\
40c5\
19k5\
11b2\
6s2\
20d1\
33a4\
11b1\
20d2\
35l5\
0m1\
18s2

- Hence, we got the string 'ccccckkkkkbbssdaaaabddlllllmss' as output. It's length is 30. 
- If the second random number that is generated is 0, it accesses the char at last index of string.

### Boundary cases
If user inputs length as 0, print a newline character and exit.
If user inputs count as 0 or 1, print a newline character and exit.

If user inputs a <count> greater than <length>, throw an error and exit.

The newline character is a 0-length string. 
It also has no character which is repeated less than once (ie 0 times).
Hence, the newline character satisfies both the edge cases.s