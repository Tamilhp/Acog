#! /bin/bash

reccurance() {
old=1
new=0

for((i=1;i<$1;i++))
do
temp=$old
old=$((new*$2))
new=$(($new+$temp))
done
((total=$old+$new))
echo $total
}

reccurance 5 3
