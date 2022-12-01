#!/usr/bin/perl

use warnings;
use POSIX qw/floor/;    # POSIX module for using floor function

$final_string = "";     # finally generated string
$temp_string = "";      # temporary variable to store partially generated string
$par_len = 0;           # length of partially generated string  
$prev_char = "";        # character at previously generated index
$filename = "input.txt";

print("maximum length of string can be - ");
$length = <STDIN>;      # enter length in command line

if($length == 0) {      # if max length of generated string is 0
    print("below here is a 0 length string -");
    print("\n\n");        # new line is a string of 0 length
    exit;
}

print("maximum times an alphabet is repeated continuously - ");
$count = <STDIN>;       # enter count in command line

if($count <= 1){
    print("here is the string");
    print("\n\n");        # no alphabet is repeated at all
    print("no character is repeated at most once\n");
    exit;
} elsif($count > $length){      # if count is greater than length, throw error and exit
    print("count should be less than length");
    exit;
}

open(FH, '<', $filename) or die "File cannot be opened";    # file is read
$line = <FH>;           # data in the file is stored    
$string_length = length($line);     # length of data

while($par_len < $length)      # execute the block when length of generated string is less than maximum permissible length
{
    # rand function is used to generate random numbers
    # generation of random numbers
    $indRep = floor(rand($string_length)); # index_to_be_repeated 
    $timesRep = floor(rand($count)); # number of times index is repeated

    if($par_len > $length){     # break out of the loop if length of partially generated string exceeds the maximum allowed length
        last;
    }

    $char = substr($line, $indRep-1, 1); # character to be repeated

    if($char eq $prev_char || $timesRep == 0){
        next;     # continue to the next iteration if character at newly generated index is same as the character at index generated just previously
    }             # or the second randomly generated number is 0

    $par_len += $timesRep;      # updating length of partially generated string

    if($par_len > $length) {     # if the length of generated string is greater than required length
        $par_len = $par_len - $timesRep;       # return to the previous length of string
        next;                    # and continue to the next iteration
    }
    
    for($i=0; $i<$timesRep; $i++){   # concatenating the character as many times as the second randomly generated number
        $temp_string = $temp_string.$char;
    }

    print($indRep);
    print($char);
    print($timesRep);
    print("\n");

    $prev_char = $char;      # updating prev_char variable to the char at new index
}

$final_string = $temp_string;   # yayy we got our final string!

print("$final_string");
print("\n");

close;          # close the file