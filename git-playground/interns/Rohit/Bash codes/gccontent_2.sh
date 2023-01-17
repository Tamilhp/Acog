#! /bin/bash

char="G"
G="$( awk -F"${char}" '{print NF-1}' <<< "${seq}" )"
echo "$G"


char="C"
C="$(awk -F"${char}" '{print NF-1}' <<< "${seq}" )"
echo "$C"


total=$(($G+$C))
echo "total count: "
echo "$total"

str=${#seq}
echo "total sequence length: "
echo "$str"

echo "$((100*$total/$str))"
