#! /bin/bash
#! /bin/bash
seq="AAAACCCGGT"

echo $seq | tr ACGT TGCA | rev


echo "Implementing with method 2:"

awk 'BEGIN{FS=""} {for (i=NF; i>0; i--) s=s $i; print s}' <<< $seq | tr ACGT TGCA
