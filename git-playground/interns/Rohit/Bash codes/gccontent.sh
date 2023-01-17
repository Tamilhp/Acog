#! /bin/bash
seq="CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
echo "G count: "
G="$(grep -o "G" <<< "$seq" | wc -l)"
echo "$G"
echo "C count: "
C="$(grep -o "C" <<< "$seq" | wc -l)"
echo "$C"
total=$(( $G + $C ))
echo "total count: "
echo "$total"

str=${#seq}
echo "total sequence length: "
echo "$str"

echo "$(( 100*$total/$str ))"
