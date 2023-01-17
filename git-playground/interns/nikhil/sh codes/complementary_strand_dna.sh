#!/bin/bash
a='A'
c='C'
g='G'
t='T'
new_string=''

string=`rev<<<$1`

string=`echo $string | tr 'A' 't'`
string=`echo $string | tr 'T' 'a'`
string=`echo $string | tr 'G' 'c'`
string=`echo $string | tr 'C' 'g'`
string=`echo $string | tr a-z A-Z`
echo "$string"

#echo "==> $string"
#for (( i=0 ; i<${#string}; i++ )); do
#       echo "$i,$string"
#done

#echo $string | awk -v ORS="" '{ gsub(/./,"&\n") ; print }' | \
#while read char
#do
#   echo "<$char>"
#done


#if [ $char == $a ]
#then
#       $new_string=$new_string+'T'
#elif [ $char == $c ]
#then
#       $new_string=$new_string+'G'
#elif [ $char == $g ]
#then
#       $new_string=$new_string+'C'
#elif [ $char == $t ]
#then
#        $new_string=$new_string+'A'
#else
#       echo -n " "
#fi