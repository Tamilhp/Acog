#! /bin/bash
for i in A C G T; 
do grep -o $i rosalind_dna.txt | wc -l; done

