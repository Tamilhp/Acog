#! /bin/bash
#! /bin/bash

reccurance() {
parent=1
child=1

for((i=1;i<$1;i++))
do
child=$parent
temp=$(($child*$2))
parent=$(($parent+$temp))
done

echo $child
}

reccurance 5 3
