#! /bin/bash

#fibonacci sequence function
fib()
{
ind=$1
mul=$2

if (( ind <= 1 ))
 then echo 0
elif (( ind == 2 ))
 then echo 1
else
	echo $(( $(fib $((ind - 1)) $((mul)) ) +$((mul)) *  $(fib $((ind - 2)) $((mul)) ) )) 
fi
 
}
#echo  fibbonacci sequence number $1 is $(fib $1) 

fib 5 3


