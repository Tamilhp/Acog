#! /bin/bash
echo -n "Enter a num :"
read Num


f1=0
f2=1

echo " fibonacci sequence for $Num is : "
echo " " 

for (( i=0;i<=Num ;i++ ))
do 
	echo -n "$f1"
	fn=$((f1+f2))
	f1=$f2
	f2=$fn
done



