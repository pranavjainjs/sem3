# Assignment 2

*Name* : Pranav Jain \
*Roll no* : 210101078 \
*OS* : Ubuntu 22.04.1 LTS

Submitted to : Dr. Pinaki Mitra / Ms. Sumita Majhi
on Oct 14, 2022.

The zip file contains submission for Programming-Assignment-2.
It contains following sub-directories  
 - Task 1  
 - Task 2

## Task 1
Josephus Problem
It requires the use of python programming language.

### To run the program
- Enter : "python q1.py" in terminal

### Assumptions
- A person can kill any other person including himself
- No one remains at last

### Parameters input in command line
- Number of people <n>
- Skip number <k>

### Constraints
- 0 <= n <= 26
- 0 <= k

### Explanation
- First person is the killer
- The killer kills <k>th person to his left
- This prompts the person just left of the victim to be the killer
- The new killer also kills <k>th person to his left
- The killing continues until no one remains, ie, everyone is killed

### Edge cases
- If k=0, everyone kills himself
- If k<0 or n<0 or n>26, error is thrown

### Test case
Number of people sitting around table : 10
Skip number is : 3

Output -

A  kills  D
E  kills  H
I  kills  B
C  kills  G
I  kills  C
E  kills  J
A  kills  I
A  kills  A
E  kills  F
E  kills  E

10  steps until no one remains

## Task 2
8 Puzzle problem
It requires the use of python programming language.

### To run the program
- Enter : "python q2.py" in terminal

### Parameters input in command line
- initial matrix
- final matrix

### Assumptions
- Trivial final matrix is-
    1 2 3
    4 5 6
    7 8 0
- Two matrices are solvable if 0 can be shifted in one of them to obtain the other one
- Inversion count of each element is the number of numbers less than itself that are present ahead of itself in the matrix

### Explanation
- The initial and final matrices are read
- 0 is shifted to the bottom right corner in both the matrices'
- The initial position of 0 in final matrix is stored, for retracing the path later
- Now a bijective function f is constructed whose domain and range are natural numbers from 1 to 8 both inclusive
- The mapping is such that the resultant final matrix maps to the trivial final matrix, ie, 
    A B C        1 2 3
    D E F --f--> 4 5 6
    G H 0        7 8 0      .... where A,B,C... are the elements of initial matrix
- In the initial matrix, each number X is replaced by f(X)
- Now the resulting matrix is checked, if 0 can be shifted so that to obtain the trivial final matrix
- This is done by calculating the total inversion count
- The matrices are solvable if the total inversion count is even, else the matrices are not solvable
- The matrices are solved if they are solvable, and the steps are printed
- To solve the matrix, each number is dealt separately
- Firstly, 0 is shifted to the center
- Then, 1 is shifted to the index (0,0), considering all the possible arrangements of 1
- Then 2, 3 are brought to their respective indices and so on till 8
- The final matrix looks like the trivial final matrix
    1 2 3
    4 5 6
    7 8 0
- Each number is replaced by its pre-image under f
    1 2 3        A B C
    4 5 6 --g--> D E F
    7 8 0        G H 0      .... g is the inverse of f
- Now, 0 is retraced to it's original position in the final matrix
- Total number of steps = 
    Number of steps to shift 0 to bottom right in initial matrix + 
    Number of steps to solve the initial matrix and the trivial final matrix +
    Number of steps to retrace 0 to its position in final matrix + 2 (for mapping)
- This approach is better than the heuristic method as the number of steps is much lesser than that of heuristic
- also, this algorithm runs for all the cases, even in which heuristic algorithm fails

### Test case
enter 9 numbers in the initial grid
1
3
4
8
0
5
7
2
6
enter 9 numbers in the final grid
1
2
3
8
0
4
7
6
5

the initial grid is-
1 3 4
8 0 5
7 2 6

initial grid on shifting 0 to bottom right corner
1 3 4
8 2 5
7 0 6       1

1 3 4
8 2 5
7 6 0       2


the final grid is-
1 2 3
8 0 4
7 6 5

final grid on shifting 0 to bottom right corner
1 2 3
8 6 4
7 0 5

1 2 3
8 6 4
7 5 0


the mapping is-
1 ---> 1
3 ---> 3
6 ---> 5
4 ---> 6
2 ---> 2
8 ---> 4
7 ---> 7
5 ---> 8

the mapped matrix is -
1 3 6
4 2 8
7 5 0       3

Goal configuration can be achieved from given configuration

1 3 6
4 2 8
7 0 5       4

1 3 6
4 0 8
7 2 5       5

1 3 6
4 2 8
7 0 5       6

1 3 6
4 2 8
7 5 0       7

1 3 6
4 2 0
7 5 8       8

1 3 0
4 2 6
7 5 8       9

1 0 3
4 2 6
7 5 8       10

1 2 3
4 0 6
7 5 8       11

1 2 3
4 5 6
7 0 8       12

1 2 3
4 5 6
7 8 0       13

1 2 3
8 6 4
7 5 0       14

1 2 3
8 6 4
7 0 5       15

1 2 3
8 0 4
7 6 5       16

Goal configuration can be achieved in  16  steps.

