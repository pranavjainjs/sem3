#! /bin/bash

# compile the code by running "bash 210101078_Assign02.sh" in terminal

#declaration of header
echo ""
declare -a header=("Employee No." "Department" "Pay Rate" "Exempt" "Hours Worked" "Base Pay" "Overtime Pay" "Total Pay")
echo "                                                  Payroll register" 
echo ""

#printing header
#Extra whitespaces are added for styling.
echo "${header[0]}     ${header[1]}   ${header[2]}   ${header[3]}  ${header[4]}    ${header[5]}        ${header[6]}    ${header[7]}"
echo ""

#reading each line from the database
while read -r line
#printing in tabular form
do
{
  sleep 1
  echo ${line} | awk -F ' ' '$4=="N" && $5>=40 {$6=$3*$5; $7=($5-40)*$3/2; print $1, "\t\t", $2, "\t     ", $3, "\t", $4, "\t", $5, "\t\t", $6, "\t\t", $7, "\t\t", $6+$7}'
  echo ${line} | awk -F ' ' '$4=="Y" {$6=$3*$5; print $1, "\t\t", $2, "\t     ", $3, "\t", $4, "\t", $5, "\t\t", $3*$5, "\t -\t\t", $6}'
}
done < EMPLOYEE
sleep 1
echo ""
