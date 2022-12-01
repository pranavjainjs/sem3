# compile the code by running "awk -f file3.awk INVENTORY" in terminal

# beginning of the report
BEGIN {print "\n\t\t\t\t\tINVENTORY REPORT\n";}

# printing header
NR == 1 {print "Part No. \t", "price \t", "Quantity on hand \t", "Reorder print \t", "Minimum Order \t", "Order Amount", "\n";}

# printing the report
$3 < $4 {print $1, "\t\t", $2, "\t\t", $3, "\t\t", $4, "\t\t", $5, "\t\t", $4+$5-$3;}
$3 >= $4 {print $1, "\t\t", $2, "\t\t", $3, "\t\t", $4, "\t\t", $5, "\t\t", "-";}

# ending of the report
END {print "\n\t\t\t\t\tEND REPORT\n";}