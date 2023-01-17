#! /bin/bash

seq="GATGGAACTTGACTACGTAAATT"
oldstr="T"
newstr="U"
result=$(echo $seq | sed "s/$oldstr/$newstr/g")
echo "Original string : $seq"
echo "Replaced Strng : $result"

echo "Implementing with method 2: "
echo "${seq//T/U}"
