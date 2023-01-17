#!/bin/bash

a=`echo $1 | tr -cd 'A' | wc -c`
c=`echo $1 | tr -cd 'C' | wc -c`
g=`echo $1 | tr -cd 'G' | wc -c`
t=`echo $1 | tr -cd 'T' | wc -c`

echo $a $c $g $t