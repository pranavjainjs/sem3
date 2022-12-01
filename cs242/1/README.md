# Information
*Name* : Pranav Jain
*Roll no* : 210101078
*OS* : Ubuntu 22.04.1 LTS

Submitted to : Dr. Pinaki Mitra / Ms. Sumita Majhi
on Aug 18, 2022.

The zip file contains submission for Programming-Assignment-1.
It contains following sub-directories
1. Task 1
2. Task 2

## Task 1

In this sub-directory, <210101078_Assign02.awk> contains an awk script which operates on the data stored in <INVENTORY>.
End of Line Sequence is LF (otherwise awk does not read the last line).
In order to execute <210101078_Assign02.awk> navigate to 'Task 1' directory in terminal and enter - 
    >> awk -f 210101078_Assign02.awk INVENTORY 

###     210101078_Assign01.awk 
        It is the awk script which contains pattern-action statements along with BEGIN and END statements.
        The '\t' characters are inserted for styling.
        NR is a built-in variable in awk which means 'Number of records read so far'

###     INVENTORY
        It is the database on which awk script operates.
        It consists of 5 columns. 
        End of Line Sequence is LF.

## Task 2

In this sub-directory, < 210101078_Assign02.sh > contains a bash script which operates on the data stored in <EMPLOYEE>.
It is assumed that the data consists a newline character after the last entry (otherwise the last line is not read).
In order to execute < 210101078_Assign02.sh > navigate to 'Task 2' directory in terminal and enter - 
    >> bash 210101078_Assign02.sh

###     210101078_Assign02.sh
        It is the bash script which reads the data with while loop.
        Extra whitespaces are added for styling.
        After a record is read, it is echoed and output is piped to awk -F command to split the line along ' ' (white space) character.

- Base Pay = (Pay rate) * (Hours worked)
- Overtime Pay = (Pay rate) * (Hours worked - 40) * 0.5
- Total Pay = Base Pay + Overtime Pay

###     EMPLOYEE
        It is the database on which bash script operates.
        It consists of 5 columns. 
        End of Line Sequence is LF.
        After the last record, a newline character is required.